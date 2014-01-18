define([
    'underscore',
    'marionette',
    'views/create-mode/game',
    'views/create-mode/editor',
    'text!templates/create-mode/content.html'
], function (_, Marionette, GameView, EditorView, tpl) {
    'use strict';

    return Marionette.Layout.extend({
        template: _.template(tpl),
        regions: {
            game: '.r-game',
            editor: '.r-editor'
        },
        initialize: function () {
            console.log('views/create-mode/content', 'initialize');
        },
        onShow: function () {
            this.editor.show(new EditorView({locationModel: this.model}));
        },
        updateGameView: function () {
            //TODO
        }
    });
});

