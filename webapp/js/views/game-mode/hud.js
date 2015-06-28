define([
    'underscore',
    'marionette',
    'text!templates/game/hud.html',
], function (_, Marionette, tpl) {
    'use strict';

    return Marionette.ItemView.extend({
        template: _.template(tpl)
    });
});
