# -*- coding: utf-8 -*-
{
    'name': "hide_fields",

    'summary': """
        Hide and Rename Fields  
        """,

    'description': """
        Hide Fields and Rename 
        in tree, form, template view 
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'odx_vrm', 'stock', 'odx_product_custom_steel','sale_crm','sale',],

    # always loaded
    'data': [
        'report/purchase_reports.xml',
        'report/sale_report.xml',
        'views/purchase_view.xml',
        'views/sale_order_views.xml',
        'views/crm_lead_views.xml',
        'views/sale_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
