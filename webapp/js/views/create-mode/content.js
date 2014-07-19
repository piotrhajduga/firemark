define([
    'underscore',
    'marionette',
    'views/game',
    'views/create-mode/editor/toolbar',
    'views/create-mode/editor/location',
    'views/create-mode/editor/location-browser',
    'models/game',
    'models/create-mode/location',
    'models/create-mode/locations',
    'text!templates/create-mode/content.html'
], function (_, Marionette, GameView, ToolbarView, LocationView, BrowserView, GameModel, LocationModel, LocationsCollection, tpl) {
    'use strict';

    return Marionette.LayoutView.extend({
        template: _.template(tpl),
        regions: {
            toolbar: '.r-toolbar',
            game: '.r-game',
            editor: '.r-editor',
            browser: '.r-browser'
        },
        initialize: function (options) {
            this.ctx = {
                locations: new LocationsCollection()
            };
        },
        onShow: function () {
            this.showToolbar();
            this.showBrowser();
        },
        refreshLocations: function () {
            return this.ctx.locations.fetch({reset: true});
        },
        newLocation: function () {
            this.editLocation({
                model: new LocationModel()
            });
        },
        showToolbar: function () {
            this.toolbarView = new ToolbarView();
            this.listenTo(this.toolbarView, 'locations:new', this.newLocation);
            this.listenTo(this.toolbarView, 'locations:browse', this.browse);
            this.toolbar.show(this.toolbarView);
        },
        showBrowser: function () {
            this.refreshLocations().done(_.bind(function () {
                var browserView = new BrowserView({collection: this.ctx.locations});
                this.listenTo(browserView, 'locations:edit', this.editLocation);
                this.listenTo(browserView, 'locations:preview', this.previewLocation);
                this.browser.show(browserView);
            }, this));
        },
        editLocation: function (args) {
            var editorView = new LocationView(_.pick(args, 'model'));
            this.listenTo(editorView, 'locations:preview', this.previewLocation);
            this.listenTo(editorView, 'locations:refresh', this.refreshLocations);
            this.editor.show(editorView);
        },
        previewLocation: function (args) {
            var locationId = args.model.get('id'),
                gameModel = new GameModel(),
                options;
            if (_.isUndefined(locationId)) {
                options = {
                    mode: 'creator'
                }
            } else {
                options = {
                    mode: 'creator',
                    locationId: locationId
                }
            }
            gameModel.save(options).done(_.bind(function () {
                this.game.show(new GameView({
                    model: gameModel
                }));
            }, this)).fail(function () {
                console.error('gameModel sync error');
            });
        }
    });
});

