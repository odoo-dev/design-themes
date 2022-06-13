/** @odoo-module **/

import { patch } from 'web.utils';
import { useService } from '@web/core/utils/hooks';
import { WebsiteSwitcherSystray } from '@website/systray_items/website_switcher';

const { onMounted, useState } = owl;

patch(WebsiteSwitcherSystray.prototype, 'test_themes_website_switcher_systray', {
    setup() {
        this._super();

        this.orm = useService('orm');
        this.tooltips = useState({});

        onMounted(async () => {
            const themesWebsites = await this.orm.call('website', 'get_themes_preview_tooltips');
            for (const theme of themesWebsites) {
                this.tooltips[theme.id] = {
                    tooltipTemplate: 'test_themes.ThemeTooltip',
                    tooltipPosition: 'left',
                    tooltipInfo: JSON.stringify(theme.tooltip),
                };
            }
        });
    },
    template: 'test_themes.WebsiteSwitcherSystray',
});
