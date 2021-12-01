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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
{
   "name": "Purchase Order Terms And Condition",
   "author": "Ascetic Business Solution",
   "category": "Purchase",
   "summary": """Purchase Order Terms And Condition""",
   "website": "http://www.asceticbs.com",
   "description": """
                 - Added "Terms and Condition" field in purchase order
                   Terms and Condition page
                 - Added "Terms and Condition" submenu in Purchase Order
                   (Purchase => Configuration => Terms and Condition)        
                 """,
   "version": "13.0.1.0",
   "depends": ["base",
               "purchase",
               "odx_product_custom_steel", 
              ],
   "data": [
            "security/ir.model.access.csv",
            "views/purchase_order_view.xml",
            "views/res_terms_condition_view.xml",               
           ],
   "installable": True,
   "application": True,
   "auto_install": False,
}
