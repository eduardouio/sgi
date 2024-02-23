from Con import Con


class Model(object):
    def __init__(self, enterprise, year):
        self.con = Con(enterprise)
        self.year =  year

    def get_data(self):
        '''Retorna en un arreglo toda la informacion del servers'''
        orders = self.get_orders()
        return orders

    def get_orders(self):
        orders_array = []
        query = '''
                SELECT
                    DocEntry,
                    DocNum,
                    NumAtCard as 'nro_pedido',
                    U_CORDO_TIPO_NEG as 'incoterm',
                    CardCode as 'identificacion_proveedor',
                    Comments as 'observaciones',
                    CreateDate as 'date_create',
                    U_CORDO_PTO_EMB as 'ciudad_origen',
                    U_CORDO_FLETE as 'flete_aduana',
                    U_CORDO_SEGURO as 'seguro_aduana',
                    DocTotal as 'total_pedido'
                FROM OPOR
                WHERE CreateDate > '{before_year}-12-31 23:59:29'
                AND CreateDate < '{after_year}-01-01 00:00:00';
                '''
        query = query.replace('{before_year}', str(int(self.year) - 1))
        query = query.replace('{after_year}', str(int(self.year) + 1))
        result_query = self.con.run_query(query)

        for row in result_query:
            new_row = {
                'doc_entry': row[0],
                'doc_num': row[1],
                'nro_pedido': row[2],
                'incoterm': row[3],
                'identificacion_proveedor': row[4],
                'observaciones': row[5],
                'ciudad_origen': row[7],
                'flete_aduana': str(row[8]),
                'seguro_aduana': str(row[9]),
                'total_pedido': str(row[10]),
                'order_items': self.get_order_items(row[0]),
                'supplier': self.get_supplier(row[4]),
                'product': self.get_product(row[1], row[0]),
            }
            orders_array.append(new_row)

        return orders_array

    def get_order_items(self, doc_entry):
        query = '''
            SELECT	DocEntry,
                ItemCode as 'cod_contable',
                NumPerMsr  as 'cantidad_x_caja',
                Quantity as 'nro_cajas',
                Price as 'costo_caja'
            FROM POR1
            WHERE DocEntry = {doc_entry}
        '''
        query = query.replace('{doc_entry}', str(doc_entry))
        items_array = []
        items_order = self.con.run_query(query)
        for row in items_order:
            new_row = {
                'doc_entry': row[0],
                'cod_contable' : row[1],
                'cantidad_x_caja' : str(row[2]),
                'nro_cajas' : str(row[3]),
                'costo_caja' : str(row[4]),
            }
            items_array.append(new_row)

        return items_array

    def get_invoice_details(self, doc_num, one = False):
        '''Primero se obtienen los detalles de las facturas'''
        query = '''SELECT
                        DocEntry,
                        ItemCode as 'cod_contable',
                        Quantity as 'nro_cajas',
                        Price as 'costo_caja',
                        BaseDocNum
                FROM
                PCH1 WHERE BaseDocNum = {doc_num};
                '''
        query = query.replace('{doc_num}', str(doc_num))
        items_invoice_array = []
        items_invoice = self.con.run_query(query)

        for row in items_invoice:
            new_row = {
                'doc_entry': row[0],
                'cod_contable': row[1],
                'nro_cajas': str(row[2]),
                'costo_caja': str(row[3]),
                'base_doc_num': row[4],
            }

            if one:
                return new_row

            items_invoice_array.append(new_row)

        return items_invoice_array

    def get_product(self, doc_num, doc_entry):
        detail = [];

        detail_invoice = self.get_invoice_details(doc_num)
        order_detail = self.get_order_items(doc_entry)

        query = '''
                SELECT
                    ItemCode as 'cod_contable',
                    ItemName as 'nombre',
                    NumInBuy as 'cantidad_x_caja',
                    U_COD_ICE_PRODUC as 'cod_ice',
                    U_CAPACIDAD as 'capacidad',
                    U_GRADO_ALC as 'grado_alcoholico'
                FROM OITM
                WHERE ItemCode = '{item_code}';
        '''

        #si el pedido no tiene detalles no retornamos nada
        if((len(detail_invoice) == 0) and (len(order_detail) == 0)):
            return detail

        #retornamos el detalle de la factura
        if len(detail_invoice) > 0:
            detail = detail_invoice

        #retornamos el detalle del pedido
        if(len(order_detail) > 0):
            detail = order_detail


        product_array = []
        for item in detail:
            if item['cod_contable'] != None:
                query = query.replace('{item_code}', item['cod_contable'])
                product = self.con.run_query(query)
                for row in product:
                    product_array.append({
                        'cod_contable': row[0],
                        'nombre': row[1].encode('utf-8'),
                        'cantidad_x_caja': str(row[2]),
                        'cod_ice': row[3],
                        'capacidad': str(row[4]),
                        'grado_alcoholico': str(row[5]),
                 })

        return product_array

    def get_supplier(self, card_code):
        query = '''
        SELECT
            CardCode as 'identificacion_proveedor',
            CardName as 'nombre',
            Notes as 'comentarios'
        FROM OCRD where CardCode = '{card_code}';
        '''
        if card_code is None or card_code == '':
            return {}

        query = query.replace('{card_code}', card_code)

        supplier = self.con.run_query(query)
        for row in supplier:
            return {
                'identificacion_proveedor': row[0],
                'nombre': row[1],
               # 'comentarios': row[2].decode(encoding='UTF-8'),
                'comentarios': row[2],
            }
