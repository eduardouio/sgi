import requests

from logs import loggin
from orders.models import Order
from partials.models import Partial


class UpdateFiles(object):
    def update_file(self, url_document, type_documet, upload_to, id_target):
        '''Actualza un parcial o pedido, sube los datos de las liquidaciones y/o
            Dai el modulo solo permite archivos PDF, sino realiza la 
            actualizacion retorna un diccionario indicado los errores
        
        Arguments:
            url_document {string} -- Direccion web del documento pdf
            type_documet {string} -- [liquidacion|dai]
            upload_to {string} -- [pedido|parcial]
            id_target {string} -- [nro_pedido | id_parcial]
        
        Returns:
            [dict] -- Realiza
        TODO
            1.- Obtener el fichero desde internet, comprobar el tipo y disponibilidad enlace
            2.- Obtener los textos de cada uno de los documentos
            3.- Revisar que el dai sea del pedido o parcial sino informar el error
            4.- Confirmar al usuario esta informacion
            5.- Subir PDF en carpeta y enlazar al registro, para el mombre usar nro_dai | nro_liquiacion con prefijo
            6.- Actualizar el pedido en url_dai y en path_dai que le corresponda max 3
            7.- Si todas las opciones de dai estan ocupadas ver que se hace... :(
            8.- Escribir pruebas de las funcionalidades
        '''
        
        req = requests.get(url_document)
        if req.status_code  == 200:
            document = req.content
        
        loggin('e', 'No se puede obtener el documento status {}'.format(req))
        return False


    
    def update_order(self, nro_order, file):
        pass
    

    def update_partial(self, id_partial, file, type_file):
        pass
    

    def get_dai_info(self, document):
        data = {
            'nro_refrendo' : None,
            'fecha_declaracion_inicial' : None,
            'ruc_importador' : None,
            'agente_aduana' : None,
            'ruc_agente_aduana' : None,
            'nro_depacho_dai': None,
            'factura_proveedor' : None,
            'fecha_emision_factura_proveedor':None,
        }
    
        return data
    

    def get_liquidation_info(self, document):
        data = {
            'nro_liquidacion' : None,
            'ruc_importador' : None,
            'ciudad' : None,
            'arancel_advalorem' : None, 
            'arancel_advalorem_liberado' : None, 
            'arancel_advalorem_a_pagar' : None, 
            'arancel_especifico' : None,
            'arancel_especifico_liberado' : None,
            'arancel_especifico_a_pagar' : None,
            'fondinfa' : None,
            'ice_advalorem' : None,
            'ice_especifico' : None,
            'fecha_liquidacoin': None,
            'total_liquidacion' : None,
            'observacion' : None,
        }

        return data
