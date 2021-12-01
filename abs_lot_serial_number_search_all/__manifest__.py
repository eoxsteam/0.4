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
   "name": "Lot Serial Number Search All",
   "author": "Ascetic Business Solution",
   "category": "Stock",
   "summary": """Lot Serial Number Search All""",
   "website": "http://www.asceticbs.com",
   "description": """
                 - Added Master search functionality in stock.production.lot model       
                 """,
   "version": "13.0.1.0",
   "depends": ["base",
               "stock",
              ],
   "data": [
            "views/stock_production_lot_views.xml",               
           ],
   "installable": True,
   "application": True,
   "auto_install": False,
}
