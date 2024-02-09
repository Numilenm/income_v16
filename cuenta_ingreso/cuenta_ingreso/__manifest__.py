{
    'name': 'cuenta_ingreso',
    'description': """Este módulo agrega campo a contacto cuenta ingreso y cambia por defecto en líneas de factura """,
    'author': 'Numilen Monzon Soledad',
    'version': '1.0',
    'depends': ['base', 'account', 'contacts', 'sale'],
    'data': [
        'views/cuenta_views.xml',
        'views/sale_order_account_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
