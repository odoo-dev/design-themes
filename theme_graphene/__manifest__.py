{
    'name': 'Graphene Theme',
    'description': 'Light colours, thin text, clean and sharp design.',
    'category': 'Theme/Corporate',
    'summary': 'Service, Corporate, Design, Technology, Robotics, Computers, IT, Blogs',
    'sequence': 110,
    'version': '2.0.0',
    'data': [
        'data/ir_asset.xml',
        'views/images_library.xml',
        'views/customizations.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/graphene_poster.jpg',
        'static/description/graphene_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_graphene/static/src/img/pictures/bg_image_08.jpg',
        'website.s_text_image_default_image': '/theme_graphene/static/src/img/pictures/content_02.jpg',
        'website.s_parallax_default_image': '/theme_graphene/static/src/img/pictures/content_12.jpg',
        'website.s_picture_default_image': '/theme_graphene/static/src/img/pictures/content_04.jpg',
    },
    'snippet_lists': {
        'homepage': ['s_cover', 's_text_image', 's_numbers', 's_picture', 's_comparisons'],
    },
    'new_page_templates': {
        'about': {
            'full': ['s_text_block_title_about', 's_image_text_about_0', 's_text_image_about_0', 's_numbers_about_0', 's_picture_about_team', 's_quotes_carousel_about_0', 's_references_about_0'],
            "full_1": ['s_text_block_title_about', 's_three_columns_about', 's_text_block_title_about_1', 's_company_team_block_about', 's_references_about_0', 's_quotes_carousel_about_0', 's_call_to_action'],
            'mini': ['s_cover_about_0', 's_text_block_title_about_3', 's_text_block_about_0', 's_picture_about_0', 's_text_block_title_contact', 's_website_form_about_0'],
            'personal': ['s_text_cover_about_personal', 's_image_text_about_personal', 's_text_block_title_about_personal', 's_numbers_about_personal', 's_features_about_personal', 's_call_to_action'],
        },
        'landing': {
            # Blocks need to be listed for all intermediary templates to be generated
            # E.g. s_text_block_title_landing is not referenced at all in website
            #      s_image_text_about_0 is not referenced on the landing_0 page in website 
            '0': ['s_cover_soon_0'],
            '1': ['s_banner_landing', 's_features_landing', 's_masonry_block_landing', 's_call_to_action', 's_references_about_0', 's_quotes_carousel_about_0'],
            '2': ['s_cover_landing', 's_text_image_landing', 's_text_block_title_landing_service', 's_three_columns_landing_1', 's_call_to_action'],
            '3': ['s_text_cover_landing', 's_text_block_title_landing', 's_three_columns_landing', 's_showcase_landing', 's_color_blocks_2_landing', 's_quotes_carousel_about_0', 's_call_to_action'],
        },
        'gallery': {
            '0': ['s_text_block_title_gallery', 's_images_wall'],
            '1': ['s_banner_gallery', 's_text_block_gallery', 's_image_gallery', 's_picture_about_0'],
        },
        'services': {
            '0': ['s_text_block_title_services_no_padding', 's_text_block_service', 's_three_columns_service', 's_text_block_title_contact', 's_website_form_about_0'],
            '1': ['s_text_block_title_services', 's_features_grid', 's_text_block_title_faq', 's_faq_collapse', 's_call_to_action'],
            '2': ['s_text_cover_service', 's_image_text_service', 's_text_image_service', 's_image_text_service_1', 's_call_to_action'],
            '3': ['s_text_block_title_services', 's_parallax_services', 's_table_of_content', 's_call_to_action'],
        },
        'pricing': {
            '0': ['s_text_block_title_pricing', 's_comparisons', 's_text_block_pricing', 's_showcase', 's_text_block_title_faq', 's_faq_collapse', 's_call_to_action'],
            '1': ['s_carousel_menu', 's_product_catalog', 's_call_to_action'],
        },
        'team': {
            '0': ['s_text_block_title_team', 's_three_columns_team'],
            '1': ['s_text_block_title_team_no_padding', 's_image_text_team', 's_text_image_team', 's_image_text_team_1'],
            '2': ['s_text_block_title_team_no_padding', 's_company_team'],
        },
    },
    'depends': ['theme_common'],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-graphene.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_graphene/static/src/js/tour.js',
        ],
    }
}
