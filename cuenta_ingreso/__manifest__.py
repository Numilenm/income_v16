{
    'name': 'cuenta_ingreso',
    'description': """Este módulo agrega campo a contacto cuenta ingreso y cambia por defecto en líneas de factura """,
    'author': 'Numilen Monzon Soledad GECONS SAS',
    'version': '1.0',
    'depends': ['base', 'account', 'contacts', 'sale', 'account_accountant'],
    'data': [
        'views/cuenta_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
