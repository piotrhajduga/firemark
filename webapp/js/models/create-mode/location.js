define([
    'underscore',
    'backbone'
], function (_, Backbone) {
    'use strict';

    return Backbone.Model.extend({
        urlRoot: '/api/create-mode/locations',
        idAttr: 'id',
        validate: function (attributes, options) {
            if (_.isEmpty(attributes.codename)) {
                return 'codename cannot be empty';
            }
        }
    });
});
