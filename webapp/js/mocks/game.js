define([
    'faux-server'
], function (server, locations) {
    'use strict';

    var game = {
        login: 'firemark',
        mode: 'creator',
        lastAction: '2014-09-11 13:20:19',
        location: {
            codename: 'TEsaiuarwe'
        }
    };

    server.addRoutes({
        getGame: {
            urlExp: '/api/game',
            httpMethod: 'GET',
            handler: function (context) {
                console.log('fauxServer in', context);
                return _.extend(game, {
                    lastAction: new Date().toISOString()
                });
            }
        },
        startGame: {
            urlExp: '/api/game',
            httpMethod: 'POST',
            handler: function (context) {
                var loc, locationId = context.data.locationId;
                console.log('fauxServer in', context);
                if (context.data.mode === 'creator') {
                    var locations = require('mocks/create-mode/locations');
                    if (locationId && locationId != 'current') {
                        loc = _.findWhere(locations, {
                            id: locationId
                        });
                    }
                    _.extend(game, {
                        lastAction: new Date().toISOString(),
                        location: loc || game.location
                    });
                }
                return game;
            }
        },
        updateGame: {
            urlExp: '/api/game',
            httpMethod: 'PUT',
            handler: function (context) {
                console.log('fauxServer in', context);
                return _.extend(game, {
                    lastAction: new Date().toISOString(),
                });
            }
        }
    });

    return game;
});
