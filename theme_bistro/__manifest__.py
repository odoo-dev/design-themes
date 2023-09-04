{
    'name': 'Bistro Theme',
    'description': 'Bistro Theme - Restaurant, Food/Drink, Catering, Food trucks',
    'category': 'Theme/Food',
    'summary': 'Bistro, Restaurant, Bar, Pub, Cafe, Food, Catering',
    'sequence': 220,
    'version': '2.0.0',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/layout.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_columns.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_text_image.xml',
        'views/new_page_template.xml',

    ],
    'images': [
        'static/description/bistro_cover.jpg',
        'static/description/bistro_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_bistro/static/src/img/backgrounds/17.jpg',
        'website.s_picture_default_image': '/theme_bistro/static/src/img/content/picture.jpg',
        'website.s_product_catalog_default_image': '/theme_bistro/static/src/img/backgrounds/16.jpg',
        'website.s_quotes_carousel_demo_image_1': '/theme_bistro/static/src/img/backgrounds/19.jpg',
    },
    'snippet_lists': {
        'homepage': ['s_cover', 's_features', 's_picture', 's_product_catalog', 's_text_block', 's_quotes_carousel'],
        'pricing': ["s_text_image", "s_product_catalog"],
    },
    'new_page_templates': {
        'about': {
            'full': ['s_text_block_title_about', 's_image_text_about_0', 's_text_image_about_0', 's_numbers_about_0', 's_picture_about_team', 's_quotes_carousel_about_0', 's_references_about_0'],
            "full_1": ['s_text_block_title_about', 's_three_columns_about', 's_text_block_title_about_1', 's_company_team_block_about', 's_references_about_0', 's_quotes_carousel_about_0', 's_call_to_action'],
            'mini': ['s_cover_about_0', 's_text_block_title_about_3', 's_text_block_about_0', 's_picture_about_0', 's_text_block_title_contact', 's_website_form_about_0'],
            'personal': ['s_text_cover_about_personal', 's_image_text_about_personal', 's_text_block_title_about_personal', 's_numbers_about_personal', 's_features_about_personal', 's_call_to_action_about'],
        },
        'landing': {
            # Blocks need to be listed for all intermediary templates to be generated
            # E.g. s_text_block_title_landing is not referenced at all in website
            #      s_image_text_about_0 is not referenced on the landing_0 page in website 
            '0': ['s_cover_soon_0'],
            '1': ['s_banner_landing', 's_features_landing', 's_masonry_block_landing', 's_call_to_action_landing_2', 's_references_about_0', 's_quotes_carousel_about_0'],
            '2': ['s_cover_landing', 's_text_image_landing', 's_text_block_title_landing_service', 's_three_columns_landing_1', 's_call_to_action_landing'],
            '3': ['s_text_cover_landing', 's_text_block_title_landing', 's_three_columns_landing', 's_showcase_landing', 's_color_blocks_2_landing', 's_quotes_carousel_about_0', 's_call_to_action_landing_1'],
        },
        'gallery': {
            '0': ['s_text_block_title_gallery', 's_images_wall'],
            '1': ['s_banner_gallery', 's_text_block_gallery', 's_image_gallery', 's_picture_about_0'],
        },
        'services': {
            '0': ['s_text_block_title_services_no_padding', 's_text_block_service', 's_three_columns_service', 's_text_block_title_contact', 's_website_form_about_0'],
            '1': ['s_text_block_title_services_no_padding', 's_features_grid', 's_text_block_title_faq', 's_faq_collapse', 's_call_to_action'],
            '2': ['s_text_cover_service', 's_image_text_service', 's_text_image_service', 's_image_text_service_1', 's_call_to_action_landing_2'],
            '3': ['s_text_block_title_services', 's_parallax_services', 's_table_of_content', 's_call_to_action'],
        },
        'pricing': {
            '0': ['s_text_block_title_pricing', 's_comparisons', 's_text_block_pricing', 's_showcase', 's_text_block_title_faq', 's_faq_collapse', 's_call_to_action'],
            '1': ['s_carousel_menu', 's_product_catalog', 's_call_to_action_menu'],
        },
        'team': {
            '0': ['s_text_block_title_team', 's_three_columns_team'],
            '1': ['s_text_block_title_team_no_padding', 's_image_text_team', 's_text_image_team', 's_image_text_team_1'],
            '2': ['s_text_block_title_team_no_padding', 's_company_team'],
        },
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-bistro.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_bistro/static/src/js/tour.js',
        ],
    }
}
