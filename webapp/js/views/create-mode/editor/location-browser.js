define([
    'underscore',
    'marionette',
    'models/create-mode/locations',
    'text!templates/create-mode/editor/browser.html',
    'text!templates/create-mode/editor/location-row.html'
], function (_, Marionette, Locations, tpl, tplRow) {
    'use strict';

    var LocationRowView = Marionette.ItemView.extend({
        template: _.template(tplRow),
        triggers: {
            'click .t-edit': 'edit',
            'click .t-preview': 'preview'
        }
    });

    return Marionette.CompositeView.extend({
        template: _.template(tpl),
        events: {
            'click .t-close': 'close'
        },
        itemView: LocationRowView,
        itemViewContainer: 'tbody',
        itemViewEventPrefix: 'locations',
        initialize: function () {
            this.collection = new Locations();
            this.collection.fetch();
        }
    });
});
