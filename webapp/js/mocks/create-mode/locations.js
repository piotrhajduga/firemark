define([
    'faux-server'
], function (server) {
    'use strict';

    var locations = [
        {id: '2134', codename: 'testowa 1'},
        {id: '2135', codename: 'testowa 2'}
    ];

    server.addRoutes({
        list: {
            urlExp: '/api/create-mode/locations',
            httpMethod: 'GET',
            handler: function (context) {
                console.log('fauxServer in', context);
                return locations;
            }
        },
        create: {
            urlExp: '/api/create-mode/locations',
            httpMethod: 'POST',
            handler: function (context) {
                console.log('fauxServer in', context);
                var loc = _.extend({
                    id: _.uniqueId()+''
                }, context.data);
                locations.push(loc);
                return loc;
            }
        },
        update: {
            urlExp: '/api/create-mode/locations/:id',
            httpMethod: 'PUT',
            handler: function (context, id) {
                console.log('fauxServer in', context, id);
                var loc = _.findWhere(locations, {id: id+''});
                _.extend(loc, _.omit(context.data, 'id'));
                return loc;
            }
        },
        get: {
            urlExp: '/api/create-mode/locations/:id',
            httpMethod: 'GET',
            handler: function (context, id) {
                console.log('fauxServer in', context, id);
                return _.findWhere(locations, {id: id});
            }
        }
    }, 'locations');

    return locations;
});
