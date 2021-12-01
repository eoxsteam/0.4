# -*- coding: utf-8 -*-

{
    "name": "Multi-selection for one2many fields",
    "version": "13.0.1.0.0",
    "summary": "This widget adds the capability for selecting multiple records in one2many fields"
               " and work on those records",
    "description": '''
        Description
        Add widget="one2many_selectable"
        You can get the selected records in python function, a simple python function is as follows:
    ''',
    "category": "Web",
    "depends": [
        'web', "sale",
    ],
    "data": [
        "view/web_assets.xml",
    ],
    "qweb":[
        'static/src/xml/widget_view.xml',
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
}
