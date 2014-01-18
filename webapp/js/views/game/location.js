define([
    'underscore',
    'marionette',
    'text!templates/game/location.html',
], function (_, Marionette, tpl) {
    'use strict';

    return Marionette.ItemView.extend({
        template: _.template(tpl)
    });
});
