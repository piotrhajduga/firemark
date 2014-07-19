define([
    'marionette'
], function (Marionette) {
    'use strict';

    return Marionette.AppRouter.extend({
        appRoutes: {
            '': 'createMode',
            'creator': 'createMode',
            'game': 'gameMode'
        }
    });
});
