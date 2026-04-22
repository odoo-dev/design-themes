from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_cozytoods_post_copy(self, mod):
        self.enable_view('website.template_footer_mega_columns')
        self.enable_view('website.template_header_search')
        self.enable_view('website.header_width_full')
