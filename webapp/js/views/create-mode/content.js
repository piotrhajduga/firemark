define([
    'underscore',
    'backbone',
    'marionette',
    'views/create-mode/game',
    'text!templates/create-mode/content.html'
], function (_, Backbone, Marionette, GameView, tpl) {
    'use strict';

    return Marionette.Layout.extend({
        template: _.template(tpl),
        regions: {
            game: '#game',
            creator: '#creator'
        },
        initialize: function () {
            console.log(['views/create-mode/content', 'initialize']);
            this.model = new Backbone.Model({id: 'test'});
        },
        onShow: function () {
            this.game.show(new GameView({model: this.model}));
        },
        onBeforeClose: function () {
            this.game.close();
        }
    });
});

