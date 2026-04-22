/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
        groupName: "Intro",
    },
    {
        id: 's_product_list',
        name: 'Items',
        groupName: "Columns",
    },
    {
        id: 's_carousel_intro',
        name: 'Carousel Intro',
        groupName: "Intro",
    },
    {
        id: 's_three_columns_sticky',
        name: 'Columns with Sticky',
        groupName: "Columns",
    },
    {
        id: 's_three_columns',
        name: 'Columns',
        groupName: "Columns",
    },
    {
        id: 's_references',
        name: 'References',
        groupName: "People",
    },
];

wTourUtils.registerThemeHomepageTour("cozytoods_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"cozy"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
    ...wTourUtils.insertSnippet(snippets[6]),
    ...wTourUtils.insertSnippet(snippets[7]),
    ...wTourUtils.insertSnippet(snippets[8]),
]);
