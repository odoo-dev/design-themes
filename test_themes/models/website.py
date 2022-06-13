# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api


class Website(models.Model):
    _inherit = 'website'

    @api.model
    def get_themes_preview_tooltips(self):
        websites_themes = self.env['website'].get_test_themes_websites()
        websites_with_preview_image = []
        for website in websites_themes:
            website_with_preview_image = {
                'id': website.id,
            }
            image_ids = website.theme_id.sudo().image_ids
            if image_ids:
                website_with_preview_image["tooltip"] = f"/web/image/{image_ids[0].id}"
            websites_with_preview_image.append(website_with_preview_image)
        return websites_with_preview_image

    def get_test_themes_websites(self):
        website_imd_ids = self.env['ir.model.data'].sudo().search([
            ('module', '=', 'test_themes'),
            ('model', '=', 'website'),
        ])
        return self.browse(website_imd_ids.mapped('res_id'))

    def unlink(self):
        websites_themes = self.get_test_themes_websites()
        if self in websites_themes:
            # Bypass foreign key constraint
            website_domain = [('website_id', '=', self.id)]
            self.env['ir.ui.view'].with_context(active_test=False, _force_unlink=True).search(website_domain).unlink()
            self.env['ir.attachment'].with_context(active_test=False).search(website_domain).unlink()
        return super().unlink()
