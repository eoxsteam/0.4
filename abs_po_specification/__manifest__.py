# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2021-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>. #4eb6c4
#
#################################################################################
{
    "name": "Po Specification",
    "summary": """Po Specification""",
    "vesion":"13.0.1.0",
    "category": "Purchase",
    "website": "http://www.asceticbs.com",
    "author": "Ascetic Business Solution",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": ["base",
                "odx_product_custom_steel",
                "abs_crane"
               ],
    "data": [
             'data/res_dfars_domestic_data.xml',
             'data/res_edge_data.xml',
             'data/res_gauge_data.xml',
             'data/res_eye_pos_data.xml',
             'data/res_gauge_type_data.xml',
             'data/res_nct_ct_data.xml',
             'data/res_oil_dry_data.xml',
             'data/res_receive_tag_data.xml',
             'data/res_skid_cylinder_data.xml',
             'data/res_yte_data1.xml',
             "security/ir.model.access.csv",
             "views/purchase_view.xml",
             "views/purchase_order_line_hide_space.xml",
             "views/purchase_order_line_add_space_view.xml",
             "views/res_dfars_domestic_view.xml",
             "views/res_gauge_type_view.xml",
             "views/res_gauge_view.xml",
             "views/res_nct_ct_view.xml",
             "views/res_oil_dry_view.xml",
             "views/res_receive_tag_view.xml",
             "views/res_yet_view.xml",
             "views/res_skid_cylinder_view.xml",
             "views/res_edge_view.xml",
             "views/res_skid_cylinder_view.xml",
             "views/res_eye_pos_view.xml",
            ],
    "demo": [],
    "qweb": [],
}
