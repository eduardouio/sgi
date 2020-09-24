from django.db import models

class RightsSupport(models.Model):
    '''
    Modelo creado para implementar permisos adicionales en el sistema
    '''

    class Meta:
        managed = False   

        permissions = ( 
            ('module_costs_rights', 'Permisos globales para costos'),  
            ('module_importations_rights', 'Permisos globales para importaciones'), 
            ('module_filemanager_rights', 'Permisos globales para archivos'), 
            ('module_migrationSap_rights', 'Permisos globales para migraciones SAP'), 
            ('module_orders_rights', 'Permisos globales para Pedidos'), 
            ('module_paids_rights', 'Permisos globales para Pagos'), 
            ('module_partials_rights', 'Permisos globales para Parciales'), 
            ('module_products_rights', 'Permisos globales para productos'), 
            ('module_suppliers_rights', 'Permisos globales para proveedores'), 
            ('module_warenhouse_rights', 'Permisos globales para Bodega'), 
        )