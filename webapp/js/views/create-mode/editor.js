define([
    'underscore',
    'marionette',
    'views/create-mode/editor/toolbar',
    'views/create-mode/editor/location',
    'models/create-mode/location',
    'text!templates/create-mode/editor.html'
], function (_, Marionette, ToolbarView, LocationView, LocationModel, tpl) {
    'use strict';

    return Marionette.Layout.extend({
        template: _.template(tpl),
        regions: {
            toolbar: '.r-toolbar',
            locationBrowser: '.r-location-browser',
            location: '.r-location'
        },
        initialize: function (options) {
            this.toolbarView = new ToolbarView();
            this.listenTo(this.toolbarView, 'newLocation', this.newLocation);
        },
        onShow: function () {
            this.toolbar.show(this.toolbarView);
        },
        newLocation: function () {
            this.location.show(new LocationView({
                locationModel: new LocationModel()
            }));
        }
    });
});
