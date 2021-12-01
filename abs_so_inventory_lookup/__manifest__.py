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
    "name": "So Inventory Lookup",
    "description": "Sale Order Add Page Inventory Lookup Add Buttons",
    "summary": """So Inventory Lookup""",
    "vesion": "13.0.1.1",
    "category": "Sales",
    "website": "http://www.asceticbs.com",
    "author": "Ascetic Business Solution",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": ["base",
                "abs_inventory_lookup",
                "one2many_selection",
                ],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_view.xml",
    ],
    "demo": [],
    "qweb": [],
}
