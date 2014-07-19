define([
    'underscore',
    'marionette',
    'models/create-mode/locations',
    'text!templates/create-mode/editor/browser.html',
    'text!templates/create-mode/editor/location-row.html'
], function (_, Marionette, Locations, tpl, tplRow) {
    'use strict';

    var LocationRowView = Marionette.ItemView.extend({
        tagName: 'tr',
        template: _.template(tplRow),
        modelEvents: {
            'change': 'render'
        },
        triggers: {
            'click .t-edit': 'edit',
            'click .t-preview': 'preview'
        }
    });

    return Marionette.CompositeView.extend({
        template: _.template(tpl),
        collectionEvents: {
            'reset': 'render'
        },
        childView: LocationRowView,
        childViewContainer: 'div.browser',
        childViewEventPrefix: 'locations'
    });
});
