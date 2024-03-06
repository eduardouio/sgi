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
        'empresa': 'cordovez',
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
        'database': 'appCordovez',
        'db_host': 'host.docker.internal',
        'db_port': '3306',
        'db_user': 'cordovez',
        'db_passwd': 'E##$%%lian.2011',
        'secret_key': 'sj-z02b^$ifmzup+&qb+6!fi4mgbah_n3ddss@9m4=e0u$fdrr',
        'url_almagro_report': 'https://almanet.almagro.com.ec/almCryReport.aspx?Enlace=0021790023516001{}/{}/{}',
        'almagro_user': 'MSALA',
        'almagro_paa': 'almagro2018',
        'safetrack': {
            'login_data': {
               'username': 'evillota',
                'password': 'Evillota2022!',
                'grant_type': 'password',
                'client_id': 'safetrack-cli',
            },
            'sub': '4e6b02f1-c83b-47a2-a76e-663569e8c71b',
            'url_login': 'https://auth.bdo.safetrack.cloud/auth/realms/safetrack/protocol/openid-connect/token',
            'url_validate_tag': 'https://bdo.safetrack.cloud/api/v1/unique-mark/validate-activate/{}/1e000ba2-7a75-4490-9e0a-9d011a63c136/{}',
            'url_validate_range': 'https://bdo.safetrack.cloud/api/v1/unique-mark/filter/',
            'url_activate_range': 'https://bdo.safetrack.cloud/api/v1/unique-mark/activate/range',
            'url_activate_tag': 'https://bdo.safetrack.cloud/api/v1/unique-mark/activate/individual',
            'wallet': {
                'business_id': '1e000ba2-7a75-4490-9e0a-9d011a63c136',
                'network': 'polygon',
                'networkAddress': '0xA62980eFB254AC2F1e9D028d710f7dFD6746D0FD',
                'networkPk': '0x44a9e1316b1d67ebef0cec0e82b7819d26e394b648f2746ccc4a2e5e42531956',
                'userId': '4e6b02f1-c83b-47a2-a76e-663569e8c71b',
                'networkProvider': 'https://matic-mumbai.chainstacklabs.com',
            }
        }
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
        'url_bottle_sap': 'http://192.168.0.198:8000/cordovez/',
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
        'safetrack': {
            'login_data': {
                'username': 'evillota',
                'password': 'Evillota2022!',
                'grant_type': 'password',
                'client_id': 'safetrack-cli',
            },
            'sub': '4e6b02f1-c83b-47a2-a76e-663569e8c71b',
            'url_login': 'https://auth.bdo.safetrack.cloud/auth/realms/safetrack/protocol/openid-connect/token',
            'url_validate_tag': 'https://bdo.safetrack.cloud/api/v1/unique-mark/validate-activate/{}/1e000ba2-7a75-4490-9e0a-9d011a63c136/{}',
            'url_validate_range': 'https://bdo.safetrack.cloud/api/v1/unique-mark/filter/',
            'url_activate_range': 'https://bdo.safetrack.cloud/api/v1/unique-mark/activate/range',
            'url_activate_tag': 'https://bdo.safetrack.cloud/api/v1/unique-mark/activate/individual',
            'wallet': {
                'business_id': '1e000ba2-7a75-4490-9e0a-9d011a63c136',
                'network': 'polygon',
                'networkAddress': '0xA62980eFB254AC2F1e9D028d710f7dFD6746D0FD',
                'networkPk': '0x44a9e1316b1d67ebef0cec0e82b7819d26e394b648f2746ccc4a2e5e42531956',
                'userId': '4e6b02f1-c83b-47a2-a76e-663569e8c71b',
                'networkProvider': 'https://matic-mumbai.chainstacklabs.com',
            }
        }
    },
    'imnac': {
        'nombre': 'IMNAC IMPORTADORA NACIONAL CIA LTDA',
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
        'safetrack': {
            'login_data': {
                 'username': 'imnac',
                'password': 'Imnac2022!',
                'grant_type': 'password',
                'client_id': 'safetrack-cli',
            },
            'sub': 'a275994b-188f-4901-861e-9a739813550f',
            'url_login': 'https://auth.bdo.safetrack.cloud/auth/realms/safetrack/protocol/openid-connect/token',
            'url_validate_tag': 'https://bdo.safetrack.cloud/api/v1/unique-mark/validate-activate/{}/24674626-0c17-4dbc-8176-7fb3805d9efb/{}',
            'url_validate_range': 'https://bdo.safetrack.cloud/api/v1/unique-mark/filter/',
            'url_activate_range': 'https://bdo.safetrack.cloud/api/v1/unique-mark/activate/range',
            'url_activate_tag': 'https://bdo.safetrack.cloud/api/v1/unique-mark/activate/individual',
            'wallet': {
                'business_id': '24674626-0c17-4dbc-8176-7fb3805d9efb',
                'network': 'polygon',
                'networkAddress': '0x424f014e1ee8aa9b2d8C5E47700575aF925a7849',
                'networkPk': '0xb9b990e159f60ebc8942b7b3a2ce0f937dd3b67fb2c8be9110d4de74658a4875',
                'userId': 'a275994b-188f-4901-861e-9a739813550f',
                'networkProvider': 'https://matic-mumbai.chainstacklabs.com',
            }
        }
    },
    'vid': {
        'nombre': 'VIDINTERNACIONAL SA',
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
        'url_almagro_report': 'https://almanet.almagro.com.ec/almCryReport.aspx?Enlace=0021791771907001{}/{}/{}',
        'almagro_user': 'MSALA_VI',
        'almagro_paa': 'almagro2018',
        'safetrack': {
            'login_data': {
                'username': 'vidinternacional',
                'password': 'Vidinter2022!',
                'grant_type': 'password',
                'client_id': 'safetrack-cli',
            },
            'sub': 'df8c7f43-66b2-470f-a72f-cc6d0e1f042e',
            'url_login': 'https://auth.bdo.safetrack.cloud/auth/realms/safetrack/protocol/openid-connect/token',
            'url_validate_tag': 'https://bdo.safetrack.cloud/api/v1/unique-mark/validate-activate/{}/ac1e614f-9738-42e0-8e05-7b169baac68e/{}',
            'url_validate_range': 'https://bdo.safetrack.cloud/api/v1/unique-mark/filter/',
            'url_activate_range': 'https://bdo.safetrack.cloud/api/v1/unique-mark/activate/range',
            'url_activate_tag': 'https://bdo.safetrack.cloud/api/v1/unique-mark/activate/individual',
            'wallet': {
                'business_id': 'ac1e614f-9738-42e0-8e05-7b169baac68e',
                'network': 'polygon',
                'networkAddress': '0xFDE38b06eCE38b6DA8c07c64EE806EadaE548cfF',
                'networkPk': '0xeee43c1734e565028981f30700c64dfead4e84ebcdf324605a00c46eebce0850',
                'userId': 'df8c7f43-66b2-470f-a72f-cc6d0e1f042e',
                'networkProvider': 'https://matic-mumbai.chainstacklabs.com',
            }
        }
    },

}

CMT_DEBUG = True
NAME_ENTERPRISE = BASE_DIR.split('/')[-1]
EMPRESA = DATOS_EMPRESAS['test']

if EMPRESA['empresa'] != 'test':
    CMT_DEBUG = True
