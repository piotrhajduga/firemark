define([
    'underscore',
    'faux-server'
], function (_, server) {
    'use strict';

    var logicBricks = [
        {
            id: 'text',
            properties: {
                contents: {
                    type: 'text'
                }
            }
        },
        {
            id: 'exits',
            properties: {
                list: {
                    type: 'list',
                    itemType: 'exit'
                }
            }
        }
    ];

    server.addRoutes({
        list: {
            urlExp: '/api/create-mode/logic-bricks',
            httpMethod: 'GET',
            handler: function (context) {
                console.log('fauxServer in', context);
                return _.map(logicBricks, function (brick) {
                    return _.omit(brick, _.functions(brick));
                });
            }
        },
        get: {
            urlExp: '/api/create-mode/logic-bricks/:id',
            httpMethod: 'GET',
            handler: function (context, id) {
                console.log('fauxServer in', context, id);
                var brick = _.findWhere(logicBricks, {id: id});
                return _.omit(brick, _.functions(brick));
            }
        }
    }, 'logicBricks');

    return logicBricks;
});
