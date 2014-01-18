define([
    'underscore',
    'marionette',
    'views/game',
    'views/create-mode/editor/toolbar',
    'views/create-mode/editor/location',
    'views/create-mode/editor/location-browser',
    'models/game',
    'models/create-mode/location',
    'text!templates/create-mode/content.html'
], function (_, Marionette, GameView, ToolbarView, LocationView, BrowserView, GameModel, LocationModel, tpl) {
    'use strict';

    return Marionette.Layout.extend({
        template: _.template(tpl),
        regions: {
            toolbar: '.r-toolbar',
            game: '.r-game',
            editor: '.r-editor'
        },
        initialize: function (options) {
            console.log('views/create-mode/content', 'initialize');
            this.toolbarView = new ToolbarView();
            this.listenTo(this.toolbarView, 'locations:new', this.newLocation);
            this.listenTo(this.toolbarView, 'locations:browse', this.browse);
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
            this.listenTo(browserView, 'locations:preview', this.previewLocation);
            this.editor.show(browserView);
        },
        editLocation: function (args) {
            var editorView = new LocationView(_.pick(args, 'model'));
            this.listenTo(editorView, 'locations:preview', this.previewLocation);
            this.editor.show(editorView);
        },
        previewLocation: function (args) {
            this.game.show(new GameView(_.pick(args, 'model')));
        }
    });
});

