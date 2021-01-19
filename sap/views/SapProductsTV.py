import json
from urllib.request import urlopen

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from logs.app_log import loggin
from products.models import Product


# /sap/productos/
class SapProductsTV(LoginRequiredMixin, TemplateView):
    template_name = 'sap/productos-sap.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Obteniendo lista de productos de SAP')
        resource = urlopen(settings.EMPRESA['url_bootle_sap'])
        products = json.load(resource)
        context = self.get_context_data(**kwargs)
        self.complete_none(products)
        context['data'] = {
            'title_page': 'Productos SAP',
            'products': products
        }

        return self.render_to_response(context)

    def check_diff(self):
        """
        Comprueba los productos que tienen diferencias con SAP
        TODO Realizar una comprobacion de los productos con SAP, 
            mediante un GET['check']

        """
        pass

    def complete_none(self, products_sap):
        """
            Completa la información de los productos con la de SAP
            siempre y cuando el producto no la tenga o sea None
        """
        sgi_products = Product.get_all()

        for sgi_p in sgi_products:
            for sap_p in products_sap['data']:
                if sgi_p.cod_contable == sap_p['cod_contable']:
                    loggin('i', 'Producto {} encontrado'.format(
                        sgi_p.cod_contable
                    ))
                    sgi_p.nombre_extrangero = sap_p['nombre_extrangero']
                    sgi_p.cod_ice = sap_p['cod_ice']
                    reg_san = '' if not bool(sap_p['nro_registro_sanitario']) else sap_p['nro_registro_sanitario'].upper()
                    reg_san = reg_san.replace('REG SAN', '')
                    reg_san = reg_san.replace('REGISTRO SANITARIO', '')
                    reg_san = reg_san.replace('NO.', '')
                    pos = ([p for p, char in enumerate(reg_san) if char == '/'])
                    if pos:
                        reg_san = reg_san[:pos[0]]

                    reg_san = reg_san.strip()
                    reg_san = reg_san.replace(' ', '-')
                    if reg_san.__len__() < 26:
                        print("update producto set nro_registro_sanitario = '{}' where cod_contable =  '{}' ;".format(reg_san, sgi_p.cod_contable))
                    if bool(reg_san):
                        sgi_p.nro_registro_sanitario = reg_san

                    #sgi_p.save() 
