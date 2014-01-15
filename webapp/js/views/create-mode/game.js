define([
    'underscore',
    'marionette',
    'text!templates/create-mode/game.html'
], function (_, Marionette, tpl) {
    'use strict';

    return Marionette.Layout.extend({
        template: _.template(tpl),
        ui: {
            bricks: '.bricks'
        },
        initialize: function (options) {
            this.model = options.model;
        },
        onRender: function () {
            var bricks = this.model.get('bricks');
            this.ui.bricks.empty();
            _.each(bricks, this.appendBrick, this);
        },
        appendBrick: function (brick) {
            var self = this;
            require(['bricks/' + brick.name + '/view'], function (View) {
                var view = new View({data: brick.data});
                self.ui.bricks.append(view.render().$el);
            });
        }
    });
});
