define([
    'faux-server'
], function (server) {
    'use strict';

    var locations = [];

    server.addRoutes({
        getLocations: {
            urlExp: '/api/create-mode/locations',
            httpMethod: 'GET',
            handler: function (context) {
                console.log('fauxServer in', context);
                return locations;
            }
        },
        createLocation: {
            urlExp: '/api/create-mode/locations',
            httpMethod: 'POST',
            handler: function (context) {
                console.log('fauxServer in', context);
                var loc = _.extend({
                    id: _.uniqueId()
                }, context.data);
                locations.push(loc);
                return loc;
            }
        },
        updateLocation: {
            urlExp: '/api/create-mode/locations/:id',
            httpMethod: 'PUT',
            handler: function (context, id) {
                console.log('fauxServer in', context, id);
                var loc = _.findWhere(locations, {id: id});
                _.extend(loc, _.omit(context.data, 'id'));
                return loc;
            }
        },
        getLocation: {
            urlExp: '/api/create-mode/locations/:id',
            httpMethod: 'GET',
            handler: function (context, id) {
                console.log('fauxServer in', context, id);
                return _.findWhere(locations, {id: id});
            }
        }
    });
});
