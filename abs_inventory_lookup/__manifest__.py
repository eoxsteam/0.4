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
   "name": "Inventory Lookup",
   "author": "Ascetic Business Solution",
   "category": "Stock",
   "summary": """Inventory Lookup""",
   "website": "http://www.asceticbs.com",
   "description": """
                 - Added "Inventory Lookup" menu in invetory module
                 - Added "By Item Info" and "By Chemistries" sub menu
                 - Open wizard by clicking on submenu       
                 """,
   "version": "13.0.1.0",
   "depends": ["base",
               "stock",
               "abs_po_specification",
               "abs_lot_serial_number_ui",
              ],
   "data": [
            "wizard/by_item_info_wizard_view.xml",
            "wizard/by_chemistries_wizard_view.xml",               
           ],
   "installable": True,
   "application": True,
   "auto_install": False,
}
