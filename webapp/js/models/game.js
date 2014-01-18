define([
    'underscore',
    'backbone',
    'utils/error-builder'
], function (_, Backbone, ErrorBuilder) {
    'use strict';

    return Backbone.Model.extend({
        urlRoot: '/api/game',
        validate: function (attrs, options) {
            var eb = new ErrorBuilder({
                validators: {
                    loginNotSet: {
                        message: 'login is not set',
                        check: function (attrs) { return _.has(attrs, 'login'); }
                    },
                    loginEmpty: {
                        message: 'login is empty',
                        check: function (attrs) { return _.isEmpty(attrs.login); }
                    },
                    passwordNotSet: {
                        message: 'password is not set',
                        check: function (attrs) { return _.has(attrs, 'login'); }
                    }
                }
            });
            eb.validate(attrs);
            if (!eb.isEmpty()) return eb.errors;
        }
    });
});
