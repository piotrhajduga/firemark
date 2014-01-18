define([
    'underscore',
    'marionette',
    'vendor/Marionette.BossView',
    'views/game/location',
    'text!templates/game.html',
], function (_, Marionette, BossView, LocationView, tpl) {
    'use strict';

    return BossView.extend({
        template: _.template(tpl),
        subViews: {
            location: function () {
                return new LocationView({
                    model: Marionette.getOption(this, 'model')
                });
            }
        },
        subViewContainers: {
            location: '.r-location'
        },
        modelEvents: {
            'change': 'render'
        },
        initialize: function (options) {
            this.model = options.model;
        }
    });
});
