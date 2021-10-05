"""
Archivo encargado de realizar el analisis de los pedidos a importar desde
SAP importa de forma automatica los pedido que no estan en el sistema
"""
import json
from decimal import Decimal
from random import randint

from django.db import DataError, IntegrityError
from logs.app_log import loggin
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from products.models import Product
from suppliers.models import Supplier


class SAPImporter(object):

    def check_orders(self, data):
        data = json.loads(data)

        if not data['data']:
            return []

        orders_verified = self.verify_orders(data['data'])

        return orders_verified

    def verify_orders(self, orders):
        """verifica los pedidos si no existen en la base local entonces
        retorna una instancia del pedido

        Args:
            ordes (list): Listado de pedidos retornados por SAP
        """
        created_orders = []
        orders = [o for o in orders if o['nro_pedido'] is not None]
        for order in orders:
            order_sgi = Order.get_by_order(
                order['nro_pedido'].replace('/', '-')
            )
            if order_sgi is None:
                origen = order['ciudad_origen']
                origin_country = ''
                origin_city = ''
                pos = ([p for p, char in enumerate(origen) if char == '/'])
                pos = pos[0]
                if pos:
                    origin_country = origen[:pos]
                    origin_city = origen[pos+1:]
                    origin_city.strip()
                    origin_country.strip()

                order_sgi = Order(
                    nro_pedido=order['nro_pedido'].replace('/', '-'),
                    regimen=order['nro_refrendo'],
                    proveedor=order['supplier']['nombre'],
                    flete_aduana=Decimal(order['flete_aduana']),
                    seguro_aduana=Decimal(order['seguro_aduana']),
                    incoterm=order['incoterm'].upper(),
                    pais_origen=origin_country,
                    ciudad_origen=origin_city,
                    nro_proforma='',
                    comentarios=order['observaciones'],
                    observaciones=order['observaciones'],
                    id_user=1
                )
                try:
                    order_sgi.save()
                    loggin('i', 'Pedido Creado Correctamente')
                    status, message = self.create_invoice(order_sgi, order)

                    if status is False:
                        loggin('i', 'Se elimina el pedido {}'.format(
                            order_sgi.nro_pedido
                        ))
                        order_sgi.delete()

                    created_orders.append({
                        'order': order,
                        'status': status,
                        'message': message
                    })

                except IntegrityError as e:
                    print("Informacion Incompleta {}".format(order_sgi.nro_pedido))
                    loggin('e', 'informacion incompleta {}'.format(e))

                except DataError as e:
                    loggin('e', 'Error en datos {}'.format(e))

        return created_orders

    def create_invoice(self, order_sgi, order):
        """Importa el pedido al Sistema de importaciones genera la
         factura y los items de la misma

        Args:
            order (dict): Pedido modelo SGI guardado
            order (dict): Pedido con todos los detalles
        """
        supplier = Supplier().get_by_ruc(order['identificacion_proveedor'])

        if supplier is None:
            return (False, 'Proveedor {} no existe'.format(
                order['identificacion_proveedor']
            ))

        invoice_number = (
            'SF-' +
            supplier.nombre[:5] +
            str(randint(111111, 999999))
        )
        money = supplier.moneda_transaccion
        type_change = Decimal(1) if money == 'DOLARES' else Decimal(1.25)

        order_invoice = OrderInvoice(
            identificacion_proveedor=supplier,
            proveedor=supplier.nombre,
            nro_pedido=order_sgi,
            id_factura_proveedor=invoice_number,
            valor=Decimal(order['total_pedido']) / type_change,
            moneda=money,
            tipo_cambio=type_change,
            id_user=1
        )

        try:
            order_invoice.save()
            loggin('i', 'Factura correctamente guardada')
            status, message = self.create_order_items(order_invoice, order)

            if status is False:
                OrderInvoiceDetail.delete_by_order_invoice(
                    order_invoice.id_factura_proveedor
                )
                order_invoice.delete()
                loggin('i', 'Se elimina la factura creada con sus items')

            return(status, message)

        except IntegrityError as e:
            loggin('e', 'informacion incompleta {}'.format(e))

        except DataError as e:
            loggin('e', 'Error en datos {}'.format(e))

        return (False, 'Problemas con la factura del proveedor')

    def create_order_items(self, order_invoice, order):
        """Registramos los items de la factura en el sistema

        Args:
            order_invoice (OrderInvoice): Orderinvoice Model instance
            order (dict): All order sap information
        """
        if not order['order_items'].__len__():
            return(False, 'El pedido no tiene productos')

        for item in order['order_items']:
            product = Product.get_by_cod_contable(item['cod_contable'])
            if product is None:
                return (False, 'Uno de los productos no existe {}'.format(
                    item['cod_contable']
                ))

            invoice_item = OrderInvoiceDetail(
                id_pedido_factura=order_invoice,
                cod_contable=product,
                product=product.nombre,
                costo_caja=Decimal(item['costo_caja']),
                nro_cajas=int(float(item['nro_cajas'])),
                cajas_importadas=Decimal(item['nro_cajas']),
                cantidad_x_caja=Decimal(item['cantidad_x_caja']),
                capacidad_ml=product.capacidad_ml,
                grado_alcoholico=product.grado_alcoholico,
                costo_botella=(
                    Decimal(item['costo_caja']) /
                    Decimal(item['cantidad_x_caja'])
                ),
                id_user=1
            )

            try:
                invoice_item.save()
                loggin('i', 'Item Correctamente salvado')

            except IntegrityError as e:
                loggin('e', 'informacion incompleta {}'.format(e))
                return (False, 'La informacion producto incompleta {}'.format(
                    product
                ))

            except DataError as e:
                loggin('e', 'Error en datos {}'.format(e))
                return (False, 'Error en datos producto {}'.format(
                    product
                ))

        return(True, 'Productos importados correctamente')
