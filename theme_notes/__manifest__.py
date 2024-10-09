{
    'name': 'Notes & Play Theme',
    'description': 'Notes & Play Theme',
    'category': 'Theme/Retail',
    'summary': 'Band, Musics, Sound, Concerts, Artists, Records, Event, Food, Stores',
    'sequence': 280,
    'version': '2.1.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_cta_box.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_striped.xml',
        'views/snippets/s_striped_top.xml',
        'views/snippets/s_cards_grid.xml',
        'views/snippets/s_carousel_intro.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_images_mosaic.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_company_team_basic.xml',
        'views/snippets/s_masonry_block.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_freegrid.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_card_offset.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_image_title.xml',
        'views/snippets/s_framed_intro.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_image_text_overlap.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_company_team_detail.xml',
        'views/snippets/s_company_team_shapes.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_features_wall.xml',
        'views/snippets/s_sidegrid.xml',
        'views/snippets/s_features_grid.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_parallax.xml',
        'views/snippets/s_pricelist_cafe.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_quotes_carousel_minimal.xml',
        'views/snippets/s_unveil.xml',
        'views/snippets/s_key_benefits.xml',
        'views/snippets/s_pricelist_boxed.xml',
        'views/snippets/s_image_hexagonal.xml',
        'views/snippets/s_striped_center_top.xml',
        'views/snippets/s_company_team_card.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_quadrant.xml',
        'views/snippets/s_intro_pill.xml',
        'views/snippets/s_big_number.xml',
        'views/snippets/s_image_frame.xml',
        'views/snippets/s_wavy_grid.xml',
        'views/snippets/s_shape_image.xml',
        'views/snippets/s_text_cover.xml',
        'views/snippets/s_empowerment.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/notes_description.jpg',
        'static/description/notes_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.library_image_03': '/theme_notes/static/src/img/content/library_image_19.jpg',
        'website.library_image_05': '/theme_notes/static/src/img/content/library_image_05.jpg',
        'website.library_image_10': '/theme_notes/static/src/img/content/library_image_10.jpg',
        'website.library_image_14': '/theme_notes/static/src/img/content/library_image_14.jpg',
        'website.library_image_16': '/theme_notes/static/src/img/content/library_image_16.jpg',
        'website.s_carousel_default_image_2': '/theme_notes/static/src/img/content/content_img_23.jpg',
        'website.s_cover_default_image': '/theme_notes/static/src/img/content/content_img_14.jpg',
        'website.s_image_text_default_image': '/theme_notes/static/src/img/content/content_img_16.jpg',
        'website.s_three_columns_default_image_1': '/theme_notes/static/src/img/content/content_img_18.jpg',
        'website.s_three_columns_default_image_2': '/theme_notes/static/src/img/content/content_img_19.jpg',
        'website.s_three_columns_default_image_3': '/theme_notes/static/src/img/content/content_img_20.jpg',
        'website.s_text_image_default_image': '/theme_notes/static/src/img/content/content_img_15.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_framed_intro', 's_image_text', 's_three_columns', 's_images_wall', 's_text_image', 's_company_team_shapes', 's_title', 's_call_to_action'],
    },
    'new_page_templates': {
        'about': {
            'personal': ['s_text_cover', 's_image_text', 's_text_block_h2', 's_numbers', 's_features', 's_call_to_action'],
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
