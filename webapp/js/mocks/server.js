define([
    'faux-server'
], function (server) {
    'use strict';

    var originalAddRoutes = server.addRoutes;

    server.addRoutes = function (routes, prefix) {
        var newRoutes = {};
        _.each(routes, function (route, key) {
            newRoutes[prefix + ':' + key] = route;
        });
        originalAddRoutes.call(server, newRoutes);
    };

    require([
        'mocks/create-mode/locations',
        'mocks/create-mode/logic-bricks',
        'mocks/game'
    ]);

    console.log("fauxServer", server.getVersion());
});
