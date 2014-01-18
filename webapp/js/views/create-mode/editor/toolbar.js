define([
    'underscore',
    'marionette',
    'text!templates/create-mode/editor/toolbar.html'
], function (_, Marionette, tpl) {
    'use strict';

    return Marionette.ItemView.extend({
        template: _.template(tpl),
        tools: {
            newLocation: {
                className: 't-new-location',
                text: '+location'
            }
        },
        triggers: {
            'click .t-new-location': 'newLocation'
        },
        serializeData: function () {
            return {tools: this.tools};
        }
    });
});
