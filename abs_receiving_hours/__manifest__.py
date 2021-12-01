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
   "name": "Receiving Hours",
   "author": "Ascetic Business Solution",
   "category": "Sales",
   "summary": """Receiving Hours""",
   "website": "http://www.asceticbs.com",
   "description": """
                 - Added "Time Range" submenu in Purchase Order
                   (Sale => Configuration => Time Range) 
                 - Added "Week Day Range" submenu in Purchase Order
                   (Sale => Configuration => Week Day Range)
                 - Added "Time Range" and "Day Range" field in res.partner form view          
                 """,
   "version": "13.0.1.0",
   "depends": ["base",
               "sale_management",
              ],
   "data": [
            "security/ir.model.access.csv",
            "views/res_receiving_hours_view.xml",
            "views/res_receiving_week_day_view.xml",
            "views/res_partner_view.xml",                 
           ],
   "installable": True,
   "application": True,
   "auto_install": False,
}
