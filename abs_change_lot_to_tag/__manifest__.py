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
   "name": "Change Lot To Tag",
   "author": "Ascetic Business Solution",
   "category": "Stock",
   "summary": """Change Lot To Tag""",
   "website": "http://www.asceticbs.com",
   "description": """
                 - Changed the string from "Lot" to "Tag"        
                 """,
   "version": "13.0.1.1",
   "depends": ["base",
               "stock",
               "odx_freight_management",
               "odx_steel_production",
               "odx_product_custom_steel",  
              ],
   "data": [
            "views/product_view.xml",
            "views/stock_move_line_view.xml",
            "views/stock_package_view.xml",
            "views/freight_management_view.xml",
            "views/processing_instruction_view.xml",
            "views/job_order_view.xml",
            "views/account_move_view.xml",                
           ],
   "installable": True,
   "application": True,
   "auto_install": False,
}
