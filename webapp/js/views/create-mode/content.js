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

    var HidingRegion = Marionette.Region.extend({
        open: function (view) {
            this.$el.hide();
            this.$el.html(view.el);
            this.$el.slideDown("fast");
        }
    });

    return Marionette.Layout.extend({
        template: _.template(tpl),
        regions: {
            toolbar: '.r-toolbar',
            game: {
                selector: '.r-game',
                regionType: HidingRegion
            },
            editor: {
                selector: '.r-editor',
                regionType: HidingRegion
            }
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
                console.log('gameModel sync error');
            });
        }
    });
});

