define([
    'underscore',
    'backbone',
    'models/create-mode/location'
], function (_, Backbone, Location) {
    'use strict';

    return Backbone.Collection.extend({
        url: '/api/create-mode/locations',
        model: Location
    });
});
