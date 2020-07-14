# -*- coding: utf-8 -*-
import xmlrpc.client

class GisOdoo(object):
    """docstring for ."""

    def __init__(self):
        self.url = 'http://ec2-3-212-63-228.compute-1.amazonaws.com:8079'
        #self.url = 'http://localhost:8069'
        #self.url = 'http://ec2-3-212-63-228.compute-1.amazonaws.com'
        #self.db = 'Odoo12-LogistikProd'
        self.db = 'Odoo12_ETest'
        #self.db = 'Odoo12_LogistikGis'
        self.username = 'interface1@logistik.gt'
        self.password = 'interface12020'
        self.datos = []
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

        self.uid = self.common.authenticate(self.db, self.username, self.password, {})

    def validarAccesos(self):
        db = self.db
        uid = self.uid
        password = self.password
        url = self.url
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        #access me permite validar que el usuario tenga accesos al modelo (tabla).
        access = models.execute_kw(db, uid, password, 'pedidos', 'check_access_rights', ['read'], {'raise_exception': False})
        if not access:
            print("No tiene acceso al modelo (pedidos).")
            return False
        else:
            print("Si tiene acceso")
            return True

    def GR_QueryTest(self):
        db = self.db
        uid = self.uid
        password = self.password
        url = self.url
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        contacto_id = 4085

        #Ingreso de informacióndel encabezado de las rutasplanificado en el portal Gis Routes
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        register_row = [[],[{
            "FECHA_REGISTRO": "13/07/2020",
            "FECHA_ENTREGA" : "14/07/2020",
            "REFERENCIA": "GUIA-2020-001",
            "CLIENTE_CODIGO": "101001",
            "CLIENTE_NOMBRE": "Monica Lemus",
            "CLIENTE_MUNICIPIO": "Guatemala",
            "CLIENTE_DIRECCION": "18 calle 6-16 zona 10",
            "CLIENTE_TELEFONO": "42114011",
            "DESCRIPCION": "Sopas",
            "NOTAS": "Producto refrigerado",
            "PESO": 126,
            "VOLUMEN": 520,
            "PRECIO": 200,
        }]]
        p = self.models.execute_kw(db, uid, password, 'pedidos', 'Api_PedidoNuevo', register_row)
        print("-------------------------------------------------------------------------------------------------- Agregando Rutra Programada")
        print(p)

        #Busca el pidido que tenga como referencia el argumento enviado
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        register_row = [[],{"REFERENCIA": "GUIA-2020-001"}]
        p = self.models.execute_kw(db, uid, password, 'pedidos', 'Api_GetPedido', register_row)
        print("-------------------------------------------------------------------------------------------------- Agregando Rutra Programada")
        print(p)

        #Busca todos los pedidos dependiendo de un rango de fechas
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        register_row = [[],{"FECHA_DEL": "01/01/2020", "FECHA_AL": "01/12/2020"}]
        p = self.models.execute_kw(db, uid, password, 'pedidos', 'Api_GetPedido', register_row)
        print("-------------------------------------------------------------------------------------------------- Agregando Rutra Programada")
        print(p)


        return True

odoo = GisOdoo()
if odoo.validarAccesos():
    clientes = odoo.GR_QueryTest()
    #print(clientes)
