from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def update_to_sale_order_lines(self, selected_ids, name):
        if selected_ids and name:
            # print("\n\n\nbutton_update_to_sale_order_lines===============", self, selected_ids, name)
            if name == 'inventory_look_up_by_chemistries_ids':
                # print("inventory_look_up_by_chemistries_ids==================", selected_ids)
                look_up_by_chemistries_sudo = self.env['inventory.look.up.by.chemistries']
                look_up_by_chemistries_lines = look_up_by_chemistries_sudo.browse(selected_ids).exists()
                if look_up_by_chemistries_lines:
                    # print("look_up_by_chemistries_lines===============", look_up_by_chemistries_lines)
                    for line in look_up_by_chemistries_lines:
                        # print("line=================", line)
                        if line:
                            so = self.env['sale.order.line'].create({
                                'category_id': line.chem_category_id.id or line.chem_category_id,
                                'sub_category_id': line.chem_sub_category_id.id or line.chem_sub_category_id,
                                'product_id': line.chem_sub_product_id.id or line.chem_sub_product_id,
                                'product_uom_qty': line.chem_weight_min,
                                'thickness_in': line.chem_thickness_min,
                                'width_in': line.chem_width_min,
                                'length_in': line.chem_length_min,
                                'order_id': line.so_look_up_by_chemistries_id.id,
                            })
                            line.unlink()
            if name == 'inventory_look_up_by_item_ids':
                # print("inventory_look_up_by_item_ids==================", selected_ids)
                look_up_by_item_sudo = self.env['inventory.look.up.by.item']
                look_up_by_item_lines = look_up_by_item_sudo.browse(selected_ids).exists()
                if look_up_by_item_lines:
                    # print("look_up_by_item_lines===============", look_up_by_item_lines)
                    for line in look_up_by_item_lines:
                        # print("line=================", line.so_look_up_by_item_id)
                        if line:
                            so = self.env['sale.order.line'].create({
                                'category_id': line.info_category_id.id or line.info_category_id,
                                'sub_category_id': line.info_sub_category_id.id or line.info_sub_category_id,
                                'product_id': line.info_sub_product_id.id or line.info_sub_product_id,
                                'product_uom_qty': line.info_weight_min,
                                'thickness_in': line.info_thickness_min,
                                'width_in': line.info_width_min,
                                'length_in': line.info_length_min,
                                'order_id': line.so_look_up_by_item_id.id,
                            })
                            line.unlink()
        return True
