{
    'name': 'Notes & Play Theme',
    'description': 'Notes & Play Theme',
    'category': 'Theme/Retail',
    'summary': 'Band, Musics, Sound, Concerts, Artists, Records, Event, Food, Stores',
    'sequence': 280,
    'version': '2.1.0',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_carousel.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_masonry_block.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_features_grid.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_parallax.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/notes_description.jpg',
        'static/description/notes_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_carousel_default_image_1': '/theme_notes/static/src/img/content/content_img_22.jpg',
        'website.s_masonry_block_default_image_1': '/theme_notes/static/src/img/content/content_img_21.jpg',
        'website.s_text_image_default_image': '/theme_notes/static/src/img/content/content_img_15.jpg',
        'website.s_product_catalog_default_image': '/theme_notes/static/src/img/content/s_product_catalog_default_image.jpg',
        'website.s_media_list_default_image_1': '/theme_notes/static/src/img/content/content_img_25.jpg',
        'website.s_media_list_default_image_2': '/theme_notes/static/src/img/content/content_img_26.jpg',
        'website.s_media_list_default_image_3': '/theme_notes/static/src/img/content/content_img_27.jpg',
    },
    'snippet_lists': {
        'homepage': ['s_carousel', 's_masonry_block', 's_text_image', 's_product_catalog', 's_media_list', 's_company_team'],
    },
    'new_page_templates': {
        'about': {
            'full': ['s_text_block_title', 's_image_text_about_0', 's_text_image_about_0', 's_numbers_about_0', 's_picture_about_team', 's_quotes_carousel_about_0', 's_references_about_0'],
            "full_1": ['s_text_block_title', 's_three_columns_about', 's_text_block_title_about_1', 's_company_team_block_about', 's_references_about_0', 's_quotes_carousel_about_0', 's_call_to_action'],
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
            '0': ['s_text_block_title_services', 's_text_block_service', 's_three_columns_service', 's_text_block_title_contact', 's_website_form_about_0'],
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
            '1': ['s_text_block_title_team', 's_image_text_team', 's_text_image_team', 's_image_text_team_1'],
            '2': ['s_text_block_title_team', 's_company_team'],
        },
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-notes.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_notes/static/src/js/tour.js',
        ],
    }
}
