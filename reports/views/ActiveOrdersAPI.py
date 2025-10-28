from django.views.generic import View
from django.http import JsonResponse
from decimal import Decimal, InvalidOperation

from lib_src import OrderDetailProductSale
from orders.models import Order, OrderInvoice
from logs.app_log import loggin
from products.models.Product import Product


class ActiveOrdersAPI(View):

    def get(self, request, *args, **kwargs):
        loggin('i', 'Accediendo a API de pedidos activos')

        ignore_liquidated = True
        if request.GET.get('ignore_liquidated', 'off') == 'on':
            ignore_liquidated = False

        orders = Order.get_open_orders()
        order_sale = OrderDetailProductSale()
        data = []

        for my_ord in orders:
            my_order_sale = order_sale.get(
                my_ord.nro_pedido, ignore_liquidated)
            if not my_order_sale:
                continue

            order_invoice = OrderInvoice.get_by_order(my_ord.nro_pedido)
            my_order_sale['total_sale'] = 0

            # Calcular total de ventas
            for item in my_order_sale['sale']:
                my_order_sale['total_sale'] += item['nro_cajas']

            if my_order_sale['total_sale']:
                status = 'EN TRANSITO'
                if order_invoice.id_factura_proveedor.startswith('SF-'):
                    status = 'EN PRODUCCION'
                else:
                    if my_ord.regimen == '70' and my_ord.bg_isclosed:
                        status = 'CERRADO'
                    elif my_ord.regimen == '70' and my_ord.fecha_ingreso_almacenera:
                        status = 'EN ALMAGRO'
                    elif my_ord.regimen == '70' and not my_ord.fecha_ingreso_almacenera:
                        status = 'EN TRANSITO'
                    elif my_ord.regimen == '10' and my_ord.fecha_llegada_cliente:
                        status = 'EN BODEGAS PARA COSTEO'

                # Procesar cada producto en el pedido
                for sale_item in my_order_sale['sale']:
                    costo_caja = sale_item.get('costo_caja', Decimal('0.0'))
                    cantidad_x_caja = sale_item['product'].cantidad_x_caja
                    if not isinstance(costo_caja, Decimal):
                        costo_caja = Decimal(str(costo_caja))
                    if not isinstance(cantidad_x_caja, Decimal):
                        cantidad_x_caja = Decimal(str(cantidad_x_caja))
                    try:
                        unit_cost = float(costo_caja / cantidad_x_caja)
                    except (ZeroDivisionError, InvalidOperation):
                        unit_cost = 0.0
                    # Validar y completar solo los campos solicitados
                    code = sale_item.get('cod_contable', '')
                    description = sale_item['product'].product
                    multipleOrderQuantity = sale_item['product'].cantidad_x_caja
                    minimumOrderQuantity = sale_item['product'].cantidad_x_caja

                    # Si description es null o las cantidades son 0, buscar en Product
                    if not description or description == 'null' or multipleOrderQuantity == 0 or minimumOrderQuantity == 0:
                        prod = Product.get_by_cod_contable(code)
                        if prod:
                            if not description or description == 'null':
                                description = prod.nombre
                            if multipleOrderQuantity == 0:
                                multipleOrderQuantity = prod.cantidad_x_caja
                            if minimumOrderQuantity == 0:
                                minimumOrderQuantity = prod.cantidad_x_caja
                    on_hand_stock = int(sale_item.get('nro_cajas', 0) * sale_item['product'].cantidad_x_caja)
                    product_data = {
                        "location": "ALMACEN SIN IMPUESTOS IMNAC",
                        "code": code,
                        "description": description,
                        "materialType": "finished",
                        "multipleOrderQuantity": int(multipleOrderQuantity),
                        "currency": "USD",
                        "unitCost": unit_cost,
                        "minimumOrderQuantity": int(minimumOrderQuantity),
                        "unitOfMeasure": "units",
                        "supplyLeadTime": 60,
                        "onHandStock": on_hand_stock if status == 'EN ALMAGRO' else 0,
                        "transitStock": on_hand_stock if status == 'EN TRANSITO' else 0,
                        "openDemandOrders": 0,
                        "transitDays": 8,
                        "nationalGyeDays": 8,
                        "nationalUioDays": 5,
                        "CardCode": order_invoice.identificacion_proveedor.identificacion_proveedor if order_invoice and order_invoice.identificacion_proveedor else "",
                        "SuppName": order_invoice.proveedor if order_invoice else "NO DEFINIDO",
                        "status": status,
                    }
                    if not product_data['code'] in [d['code'] for d in data]:
                        data.append(product_data)
                        continue

                    for item in data:
                        if item['code'] == product_data['code']:
                            item['onHandStock'] += product_data['onHandStock']
                            item['transitStock'] += product_data['transitStock']

        data = self.append_zero_stocks(data)
        # unificar por sku
        data = self.unify_by_sku(data)
        response_data = data
        return JsonResponse(response_data, safe=False)

    def unify_by_sku(self, data):
        unified_data = []
        code_map = {}
        for item in data:
            code = item.get('code', '')
            if code in code_map:
                # Si el producto ya existe, sumar el onHandStock
                index = code_map[code]
                unified_data[index]['onHandStock'] += item['onHandStock']
            else:
                # Si es la primera vez que aparece, agregarlo a la lista
                code_map[code] = len(unified_data)
                unified_data.append(item.copy())
        return unified_data

    def append_zero_stocks(self, data):
        """Agrega todos los productos de la base que no estén en la lista con stock 0"""
        # Obtener códigos de productos que ya están en la lista
        existing_codes = {item.get('code', '') for item in data}
        # Obtener todos los productos de la base de datos
        all_products = Product.objects.all()
        for product in all_products:
            if product.cod_contable not in existing_codes:
                # Producto no está en la lista, agregarlo con stock 0
                product_data = {
                    "location": "ALMACEN SIN IMPUESTOS IMNAC",
                    "code": product.cod_contable,
                    "description": product.nombre,
                    "materialType": "finished",
                    "multipleOrderQuantity": int(product.cantidad_x_caja),
                    "currency": "USD",
                    "unitCost": 0,
                    "minimumOrderQuantity": int(product.cantidad_x_caja),
                    "unitOfMeasure": "units",
                    "supplyLeadTime": 60,
                    "onHandStock": 0,
                    "transitStock": 0,
                    "openDemandOrders": 0,
                    "transitDays": 8,
                    "nationalGyeDays": 8,
                    "nationalUioDays": 5,
                    "CardCode": product.identificacion_proveedor.identificacion_proveedor if product.identificacion_proveedor else "",
                    "SuppName": product.identificacion_proveedor.nombre if product.identificacion_proveedor else "NO DEFINIDO",
                    "status": "EN ALMAGRO"
                }
                data.append(product_data)
        return data