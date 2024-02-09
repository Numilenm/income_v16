{
    'name': 'Income Account',
    'description': """This module adds a field to contacts for income account and changes the default on invoice lines. It also extends to sales order lines.""",
    'author': 'GECONS SAS',
    'price': 250.00,
    'currency': 'USD',
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
