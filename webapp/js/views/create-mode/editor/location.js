define([
    'underscore',
    'marionette',
    'vendor/Marionette.BossView',
    'text!templates/create-mode/editor/location.html'
], function (_, Marionette, BossView, tpl) {
    'use strict';

    return BossView.extend({
        template: _.template(tpl),
        events: {
            'click .t-save': 'save',
            'submit form': 'save',
            'click .t-save-new': 'saveAsNew',
            'click .t-close': 'destroy'
        },
        subViews: {
            //logicBricksView: LogicBricksView
        },
        subViewContainers: {
            logicBricksView: '.r-logic-bricks'
        },
        ui: {
            codename: 'input[name=codename]'
        },
        initialize: function (options) {
            this.model = options.model;
        },
        modelEvents: {
            'change': 'render',
            'invalid': 'validationError'
        },
        refreshLocations: function () {
            this.trigger('locations:preview', {model: this.model});
            this.trigger('locations:refresh');
        },
        save: function (evt) {
            evt.preventDefault();
            // saving logic here
            this.model.save(this.getData()).done(_.bind(this.refreshLocations, this));
        },
        saveAsNew: function (evt) {
            evt.preventDefault();
            // saving logic here
            this.model.clear({silent: true}).save(this.getData()).done(_.bind(this.refreshLocations, this));
        },
        getData: function () {
            return {
                //logicBricks: this.logicBricksView.getData(),
                codename: this.ui.codename.val()
            };
        },
        serializeData: function () {
            return {
                location: this.model.toJSON()
            };
        },
        validationError: function () {
            alert(this.model.validationError);
        }
    });
});
