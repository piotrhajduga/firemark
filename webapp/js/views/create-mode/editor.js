define([
    'underscore',
    'marionette',
    'views/create-mode/editor/toolbar',
    'views/create-mode/editor/location',
    'views/create-mode/editor/location-browser',
    'models/create-mode/location',
    'text!templates/create-mode/editor.html'
], function (_, Marionette, ToolbarView, LocationView, BrowserView, LocationModel, tpl) {
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
            this.listenTo(this.toolbarView, 'locations:new', this.newLocation);
            this.listenTo(this.toolbarView, 'locations:browse', this.browse);
        },
        onShow: function () {
            this.toolbar.show(this.toolbarView);
        },
        newLocation: function () {
            this.location.show(new LocationView({
                locationModel: new LocationModel()
            }));
        },
        browse: function () {
            var browserView = new BrowserView();
            this.listenTo(browserView, 'locations:edit', this.editLocation);
            this.location.show(browserView);
        },
        editLocation: function (args) {
            console.log('editLocation', args);
            this.location.show(new LocationView({
                locationModel: args.model
            }));
        },
    });
});
