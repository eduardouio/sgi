"""
    Archivo de confirguracion de sistema
    Cambiar el valor de la variable para confirgurar el server
    valores posibles -> cordovez | imnac | vid | test
    ENTERPRISE_CONF = [cordovez | imnac | vid | test]
"""

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATOS_EMPRESAS = {
    'test': {
        'nombre': 'AMBIENTE DE PRUEBAS TEST',
        'empresa': 'test',
        'ruc': '1722919725001',
        'direccion': 'AV COLO 1133 Y AMAZONAS EDF ARISTA OF 500 ',
        'telefono': '022405911',
        'email': 'sgi@cordovez.com.ec',
        'url_logo': 'http://179.49.60.158:8888/img/logo_test.png',
        'url_app': 'http://localhost:8000/',
        'url_app_local': 'http://localhost:8000/',
        'url_app_importaciones': 'http://179.49.60.158:8888/cordovez/',
        'url_bottle_sap': 'http://192.168.0.198:8000/cordovez/',
        'admin_title': 'TEST',
        'database': 'test_cordovezApp',
        'db_host': 'localhost',
        'db_port': '3306',
        'db_user': 'root',
        'db_passwd': 'elian.2011',
        'secret_key': 'sj-z02b^$ifmzup+&qb+6!fi4mgbah_n3ddss@9m4=e0u$fdrr',
        'url_almagro_report': 'https://almanet.almagro.com.ec/almCryReport.aspx?Enlace=0021790023516001{}/{}/{}',
        'almagro_user': 'MSALA',
        'almagro_paa': 'almagro2018',
    },
    'cordovez': {
        'nombre': 'AGENCIAS Y REPRESENTACIONES CORDOVEZ SA',
        'empresa': 'cordovez',
        'ruc': '1790023516001',
        'direccion': 'AV 10 DE AGOSTO Y LEONARDO MURIALDO ',
        'telefono': '022405911',
        'email': 'sgi@cordovez.com.ec',
        'url_logo': 'http://179.49.60.158:8888/img/logo_cordovez.jpg',
        'url_app': 'http://179.49.60.158:5001/',
        'url_app_local': 'http://localhost:5001/',
        'url_app_importaciones': 'http://179.49.60.158:8888/cordovez/',
        'url_bottle_sap': 'http://127.0.0.1:8000/cordovez/',
        'admin_title': 'CORDOVEZ',
        'database': 'cordovezApp',
        'db_host': 'localhost',
        'db_port': '3306',
        'db_user': 'appCordovez',
        'db_passwd': '\DBGfW<7;vBa5(LB',
        'secret_key': 'sj-z02b^$ifmzup+&qb+6!fi4mgbah_n3ddss@9m4=Cordovez2021',
        'url_almagro_report': 'https://almanet.almagro.com.ec/almCryReport.aspx?Enlace=0021790023516001{}/{}/{}',
        'almagro_user': 'MSALA',
        'almagro_paa': 'almagro2018',
    },
    'imnac': {
        'nombre': 'IMNAC CIA LTDA',
        'empresa': 'imnac',
        'ruc': '1792324289001',
        'direccion': 'PAUL RIVET 227 Y JAMES ORTON',
        'telefono': '022405911',
        'email': 'sgi@imnac.com.ec',
        'url_logo': 'http://179.49.60.158:8888/img/logo_imnac.jpg',
        'url_app': 'http://179.49.60.158:5002/',
        'url_app_local': 'http://localhost:5002/',
        'url_app_importaciones': 'http://179.49.60.158:8888/imnac/',
        'url_bottle_sap': 'http://192.168.0.198:8000/imnac/',
        'admin_title': 'IMNAC',
        'database': 'imnacApp',
        'db_host': 'localhost',
        'db_port': '3306',
        'db_user': 'appCordovez',
        'db_passwd': '\DBGfW<7;vBa5(LB',
        'secret_key': 'sj-z02b^$ifmzup+&qb+6!fi4mgbah_n3ddss@9m4=Imnac2021',
        'url_almagro_report': 'https://almanet.almagro.com.ec/almCryReport.aspx?Enlace=0021792324289001{}/{}/{}',
        'almagro_user': 'MSALA_IM',
        'almagro_paa': 'almagro2018',
    },
    'vid': {
        'nombre': 'VIDINTERNACIONAL S.A.',
        'empresa': 'vid',
        'ruc': '1791771907001',
        'direccion': 'AV 10 DE AGOSTO Y LEONARDO MURIALDO ',
        'telefono': '022405911',
        'email': 'sgi@vidinternacional.com.ec',
        'url_logo': 'http://179.49.60.158:8888/img/logo_vid.jpg',
        'url_app': 'http://179.49.60.158:5003/',
        'url_app_local': 'http://localhost:5003/',
        'url_app_importaciones': 'http://179.49.60.158:8888/vid/',
        'url_bottle_sap': 'http://192.168.0.198:8000/vid/',
        'admin_title': 'VIDINTERNACIONAL',
        'database': 'vidApp',
        'db_host': 'localhost',
        'db_port': '3306',
        'db_user': 'appCordovez',
        'db_passwd': '\DBGfW<7;vBa5(LB',
        'secret_key': 'sj-z02b^$ifmzup+&qb+6!fi4mgbah_n3ddss@9m4=Vid2021',
        'url_almagro_report': 'https://almanet.almagro.com.ec/almCryReport.aspx?Enlace=0021791771907001{mm}/{dd}/{yyyy}',
        'almagro_user': 'MSALA_VI',
        'almagro_paa': 'almagro2018',
    },

}

CMT_DEBUG = True
NAME_ENTERPRISE = BASE_DIR.split('/')[-1]
ENTERPRISE_CONF = 'test' if NAME_ENTERPRISE == 'sgi' else NAME_ENTERPRISE
EMPRESA = DATOS_EMPRESAS[ENTERPRISE_CONF]

if EMPRESA['empresa'] != 'test':
    CMT_DEBUG = False
