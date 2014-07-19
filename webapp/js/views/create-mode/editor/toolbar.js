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
                text: '+location',
                trigger: 'locations:new'
            }
        },
        triggers: function () {
            var tools = Marionette.getOption(this, 'tools'),
                triggers = {};
            _.each(tools, function (tool) {
                triggers['click .' + tool.className] = tool.trigger;
            });
            return triggers;
        },
        serializeData: function () {
            return {tools: this.tools};
        }
    });
});
