# -*- coding: utf-8 -*-
{
    'name': "odoo_new",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'stock', 'website','utm'],

    'assets': {
        'web.assets_backend': [
            # 'odoo_new/static/src/js/my_library.js',

        ],

        'web.assets_frontend': [
            'odoo_new/static/src/css/my_library.css',
            'odoo_new/static/src/scss/my_library.scss',
            # 'odoo_new/static/src/js/my_library.js',
            'odoo_new/static/src/js/snippets.js'

        ]
    },

    # always loaded
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/book_borrow_views.xml',
        'views/book_detail_views.xml',
        'views/book_genre_views.xml',
        'views/res_config_setting_views.xml',
        'views/res_partner_views.xml',
        'views/product_template_views.xml',
        'views/library_menu.xml',
        'views/templates.xml',
        'views/snippets.xml'

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
