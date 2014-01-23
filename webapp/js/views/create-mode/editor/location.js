define([
    'underscore',
    'marionette',
    'vendor/Marionette.BossView',
    'views/create-mode/editor/location/exits',
    'text!templates/create-mode/editor/location.html'
], function (_, Marionette, BossView, ExitsView, tpl) {
    'use strict';

    return BossView.extend({
        template: _.template(tpl),
        events: {
            'click .t-save': 'save',
            'click .t-save-new': 'saveAsNew',
            'click .t-close': 'close'
        },
        subViews: {
            //logicBricksView: LogicBricksView
            exitsView: function () {
                console.log('new ExitsView');
                return new ExitsView({
                    exits: this.model.get('exits')
                });
            }
        },
        subViewContainers: {
            exitsView: '.r-exits',
            logicBricksView: '.r-logic-bricks'
        },
        subViewEvents: {
            exitsView: {
                'exits:reset': function () {
                    this.model.set(
                        'exits',
                        this.exitsView.collection.toJSON()
                    ).save();
                }
            }
        },
        ui: {
            codename: 'input[name=codename]'
        },
        initialize: function (options) {
            console.log('BossView.initialize');
            this.model = options.model;
        },
        modelEvents: {
            'change': function () {
                this.trigger('locations:preview', {model: this.model});
                this.render();
            },
            'invalid': 'validationError'
        },
        save: function () {
            console.log('save model', this.model.toJSON());
            // saving logic here
            this.model.save(this.getData());
        },
        saveAsNew: function () {
            console.log('save new model');
            // saving logic here
            this.model.clear({silent: true}).save(this.getData());
        },
        getData: function () {
            return {
                exits: this.exitsView.getData(),
                //logicBricks: this.logicBricksView.getData()
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
