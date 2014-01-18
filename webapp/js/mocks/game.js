define([
    'faux-server'
], function (server) {
    'use strict';

    var game = {
        login: 'firemark',
        lastAction: '2014-09-11 13:20:19',
        location: {
            codename: 'TEsaiuarwe'
        }
    };

    server.addRoutes({
        getGame: {
            urlExp: '/api/game',
            httpMethod: 'GET',
            handler: function () {
                console.log('fauxServer in', context);
                return game;
            }
        }
    });
});
