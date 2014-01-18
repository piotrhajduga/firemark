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
            'click .t-close': 'close'
        },
        subViews: {
            //exitsView: ExitsView,
            //logicBricksView: LogicBricksView
        },
        subViewContainers: {
            exitsView: '.r-exits',
            logicBricksView: '.r-logic-bricks'
        },
        ui: {
            codename: 'input[name=codename]'
        },
        initialize: function (options) {
            this.model = options.locationModel;
        },
        modelEvents: {
            'change': 'render',
            'invalid': 'validationError'
        },
        save: function () {
            console.log('save model', this.model.toJSON());
            // saving logic here
            this.model.save(this.getData());
        },
        getData: function () {
            return {
                codename: this.ui.codename.val()
                //exits: this.exitsView.getData()
                //logicBricks: this.logicBricksView.getData()
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
