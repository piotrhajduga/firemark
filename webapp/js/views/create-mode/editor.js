define([
    'underscore',
    'marionette',
    'models/create-mode/location',
    'text!templates/create-mode/editor.html'
], function (_, Marionette, ToolbarView, LocationModel, tpl) {
    'use strict';

    return Marionette.LayoutView.extend({
        template: _.template(tpl),
        regions: {
            locationBrowser: '.r-location-browser',
            location: '.r-location'
        },
        onShow: function () {
            this.toolbar.show(this.toolbarView);
        },
        newLocation: function () {
            this.editLocation({
                model: new LocationModel()
            });
        },
        browse: function () {
            var browserView = new BrowserView();
            this.listenTo(browserView, 'locations:edit', this.editLocation);
            this.location.show(browserView);
        },
        editLocation: function (args) {
            var loc = new LocationView({
                model: args.model
            });
            this.listenTo(loc, 'locations:change', function (args) {
                this.trigger('locations:change', args);
            });
            this.location.show();
        },
    });
});
