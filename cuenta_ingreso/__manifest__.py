{
    'name': 'income_account',
    'description': """This module adds a field to the contact for income account
     and changes the default on invoice lines.""",
    'author': 'Numilen Monzon Soledad',
    'version': '1.0',
    'depends': ['base', 'account', 'contacts'],
    'data': [
        'views/income_account_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
