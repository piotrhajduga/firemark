define([
    'marionette'
], function (Marionette) {
    'use strict';

    return Marionette.Controller.extend({
        initialize: function (options) {
            console.log(['controllers/main', 'initialize']);
            this.region = options.region;
        },
        createMode: function () {
            console.log(['create-mode']);
            var self = this;
            require(['views/create-mode/content'], function (View) {
                self.region.show(new View());
            });
        },
        gameMode: function () {
            console.log(['game-mode']);
            this.region.close();
        }
    });
});
