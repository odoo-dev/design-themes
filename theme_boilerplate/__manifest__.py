{
    'name': 'Boilerplate Theme',
    'description': 'Boilerplate Theme - Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Creative',
    'summary': 'Boilerplate, Startup, Redesign, Creative, Design ',
    'sequence': 167,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_cover.xml',
    ],
    'images': [
        'static/description/boilerplate_cover.webp',
        'static/description/boilerplate_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_boilerplate/static/src/img/snippets/s_cover.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_banner', 's_text_image', 's_image_text', 's_picture', 's_title', 's_masonry_block_default_template', 's_company_team', 's_showcase', 's_quotes_carousel'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_image_text'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'gap': '3',
            },
            'background': {
                'shape': {
                    'data-oe-shape-data': '{"shape":"web_editor/Connections/20", "colors":{"c5":"o-color-3"}}',
                    'element': """<div class="o_we_shape o_web_editor_Connections_20" style="background-image: url('/web_editor/shape/web_editor/Connections/20.svg?c5=o-color-3');""",
                },
            },
            'add_classes': [
                'pb80',
            ],
            'remove_classes': [
                'pb64',
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',

    'assets': {
        'website.assets_editor': [
            'theme_boilerplate/static/src/js/tour.js',
        ],
    }
}
