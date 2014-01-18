define([
    'faux-server'
], function (server) {
    'use strict';

    var locations = [];

    server.addRoutes({
        createLocation: {
            urlExp: '/api/create-mode/location',
            httpMethod: 'POST',
            handler: function (context) {
                console.log('fauxServer in: ', context);
                var loc = _.extend({
                    id: _.uniqueId()
                }, context.data);
                locations.push(loc);
                return loc;
            }
        },
        updateLocation: {
            urlExp: '/api/create-mode/location/:id',
            httpMethod: 'PUT',
            handler: function (context, id) {
                console.log('fauxServer in: ', context, id);
                var loc = _.findWhere(locations, {id: id});
                _.extend(loc, _.omit(context.data, 'id'));
                return loc;
            }
        }
    });
});
