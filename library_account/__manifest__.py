{
    'name': 'Library Account',
    'author': 'utsho',
    'depends': ['odoo_new','account'],

    'data': [
        'views/account_move.xml',
        'views/book_borrow.xml',
        'views/my_contacts.xml',
        'views/calendar_view.xml',
        'views/pivot_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}