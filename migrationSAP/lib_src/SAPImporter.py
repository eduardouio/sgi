"""
Archivo encargado de realizar el analisis de los pedidos a importar desde
SAP importa de forma automatica los pedido que no estan en el sistema
"""
import json
from datetime import datetime
from decimal import Decimal
from random import randint
from urllib.error import HTTPError
from urllib.request import urlopen

from django.conf import settings
from django.db import DataError, IntegrityError
from logs.app_log import loggin
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from products.models import Product
from suppliers.models import Supplier


class SAPImporter(object):

    def __init__(self):
        self.url_api = settings.EMPRESA['url_bottle_sap']

    def check_orders(self, year):
        loggin('i', 'Realizando peticion {}{}/'.format(self.url_api, year))
        try:
            response = urlopen(self.url_api + '{}/'.format(year))
        except HTTPError as e:
            loggin('e', 'La peticion fallo {}'.format(e))
            response = False

        if not response:
            loggin('e', 'La peticion no retorno ningun dato')
            return []

        data = json.load(response)

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

        for order in orders:
            order_sgi = Order.get_by_order(order['nro_pedido'].replace('/', '-'))
            if not order_sgi:
                origen = order['ciudad_origen']
                origin_country = ''
                origin_city = ''
                pos = ([p for p, char in enumerate(origen) if char == '/'])

                if pos:
                    origin_country = origen[:pos[0]]
                    origin_city = origen[pos[0]:]
                    origin_city.strip()
                    origin_country.strip()

                order_sgi = Order(
                    nro_pedido=order['nro_pedido'].replace('/', '-'),
                    regimen=order['nro_refrendo'],
                    flete_aduana=Decimal(order['flete_aduana']),
                    seguro_aduana=Decimal(order['seguro_aduana']),
                    incoterm=order['incoterm'],
                    pais_origen=origin_country,
                    ciudad_origen=origin_city,
                    comentarios=order['observaciones']
                )
                try:
                    order_sgi.save()
                    loggin('i', 'Pedido Creado Correctamente')
                    status, message = self.create_invoice(order_sgi, order)

                    if status is False:
                        self.clean_data(order_sgi)

                    created_orders.append({
                        'order': order_sgi,
                        'status': status,
                        'message': message
                    })

                except IntegrityError as e:
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
            return (False, 'Proveedor no existe')

        invoice_number = (
            'SF-' +
            supplier.nombre[:5] +
            str(randint(11111, 99999))
        )

        type_change = Decimal(1) if supplier.moneda_transaccion is 'DOLARES' else Decimal(1.25)

        order_invoice = OrderInvoice(
            identificacion_proveedor=supplier,
            nro_pedido=order_sgi.nro_pedido,
            id_factura_proveedor=invoice_number,
            fob_tasa_trimestral=Decimal(order['total_pedido']) / type_change,
            tipo_cambio=type_change
        )

        try:
            order_invoice.save()
            loggin('i', 'Factura correctamente guardada')
            return self.create_order_items(order_invoice, order)

        except IntegrityError as e:
            loggin('e', 'informacion incompleta {}'.format(e))

        except DataError as e:
            loggin('e', 'Error en datos {}'.format(e))

        return (False, 'Problemas con la factura del proveedor')

    def create_order_items(order_invoice, order):
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
                costo_caja=Decimal(item['costo_caja']),
                nro_cajas=int(item['nro_cajas']),
                cajas_importadas=Decimal(item['nro_cajas']),
                cantidad_x_caja=Decimal(item['cantidad_x_caja']),
                capacidad_ml=product.capacidad_ml,
                costo_botella=Decimal(item['costo_caja'])/Decimal(item['cantidad_x_caja']),
                date_create=datetime.today()
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

    def clean_data(self, order_sgi):
        """Realiza una limpieza de los datos que no fueron importados
        correctamente

        Args:
            nro_order ([type]): [description]
        """
        order_ionvoice = OrderInvoice.get_by_order(order_sgi.nro_pedido)
        if order_ionvoice:
            order_items = OrderInvoiceDetail.get_by_id_order_invoice(
                order_ionvoice.id_pedido_factura
            )

            for item in order_items:
                item.delete()

        order_ionvoice.delete()
        order_sgi.delete()
        loggin('i', 'Informacion del pedido {} eliminada correctamente')
