define([
    'underscore',
    'marionette',
    'vendor/Marionette.BossView',
    'views/game/location',
    'views/game/hud',
    'text!templates/game.html'
], function (_, Marionette, BossView, LocationView, HUDView, tpl) {
    'use strict';

    return BossView.extend({
        template: _.template(tpl),
        subViews: {
            location: function () {
                return new LocationView({
                    model: Marionette.getOption(this, 'model')
                });
            },
            hud: function () {
                return new HUDView({
                    model: Marionette.getOption(this, 'model')
                });
            }
        },
        subViewContainers: {
            location: '.r-location',
            hud: '.r-hud'
        },
        modelEvents: {
            'change': 'render'
        }
    });
});
