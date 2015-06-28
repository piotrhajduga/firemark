define([
    'marionette',
    'views/game'
], function (Marionette, GameView) {
    'use strict';

    return Marionette.Controller.extend({
        initialize: function (options) {
            console.log('controllers/main', 'initialize');
            this.region = options.region;
        },
        run: function () {
            var self = this,
                dfd,
                view;
            dfd = $.Deferred(function () {
                view = new GameView(self.state);
                self.region.show(view);
                dfd.resolve();
            });
            return dfd.promise();
        }
    });
});
