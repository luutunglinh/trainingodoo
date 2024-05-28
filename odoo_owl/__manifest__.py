# -*- coding: utf-8 -*-
{
    'name': "My owl",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'website': "http://www.example.com",
    'category': 'Tools',
    'depends': ['base', 'web'],

    'assets': {
        'web.assets_backend': [
            'odoo_owl/static/src/components/*/*.js',
            'odoo_owl/static/src/components/*/*.xml',
        ],
    },

    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/library_book_owl.xml',
        'views/res_partner.xml',
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
