import pyodbc


class Con():
    '''Objeto de coneccion a server'''
    CONF = {
        'cordovez': {
            'server': '192.168.0.189',
            'database': 'DB_CORDOVEZ_PROD',
            'username': 'appimpor',
            'password': 'Vinesa.2021',
        },
        'imnac': {
            'server': '192.168.0.189',
            'database': 'DB_IMNAC_PROD',
            'username': 'appimpor',
            'password': 'Vinesa.2021',
        },
        'vid': {
            'server': '192.168.0.189',
            'database': 'DB_VID_PROD',
            'username': 'appimpor',
            'password': 'Vinesa.2021',
        },
    }

    def __init__(self, enterprise):
        '''Intancia y retorna la coneccion a la base'''
        self.conf = self.get_conf(enterprise)
        self.cxnx = None

    def run_query(self, query):
        self.make_conection()
        cursor = self.cnxn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        self.end_conection()
        return result

    def make_conection(self):
        ''' Retorna la coneccion de base de datos '''
        self.cnxn = pyodbc.connect('DRIVER=/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.10.so.5.1;SERVER=' +
                                   self.conf['server'] + ';DATABASE=' + self.conf['database'] + ' ;UID=' + self.conf['username'] + ';PWD=' + self.conf['password'])
        return self.cnxn

    def get_conf(self, enterprise):
        '''retorna los datos para la coneccion'''
        return self.CONF[enterprise]

    def end_conection(self):
        '''Cierra la coneccion con el servidor'''
        self.cnxn.close()
