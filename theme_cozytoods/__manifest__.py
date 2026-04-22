{
    'name': 'Cozy Toods Theme',
    'description': 'Cozy Toods Theme - Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Retail',
    'summary': 'Cozy Toods, Startup, Redesign, Creative, Design, Toys, Kids, Children, Playful, Clean, Responsive, Warm',
    'sequence': 287,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/global_customizations.xml',
        'views/homepage_customizations.xml',
        'views/images_library.xml',
    ],
    'images': [
        'static/description/cozytoods_cover.webp',
        'static/description/cozytoods_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_cozytoods/static/src/img/snippets/s_cover.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_gradient', 's_product_list', 's_carousel_multi_images', 's_cards_grid', 's_two_columns_sticky', 's_reviews_wall'],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',

    'assets': {
        'website.assets_editor': [
            'theme_cozytoods/static/src/js/tour.js',
        ],
    }
}
