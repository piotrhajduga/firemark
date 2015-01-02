define([
    'underscore',
    'jquery',
    'marionette',
    'vendor/Marionette.BossView',
    'controllers/context-menu',
    'text!templates/create-mode/editor/location.html'
], function (_, $, Marionette, BossView, ContextMenu, tpl) {
    'use strict';

    return BossView.extend({
        template: _.template(tpl),
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
        events: {
            'click .t-save': 'save',
            'submit form': 'save',
            'click .t-save-as-new': 'saveAsNew',
            'click .t-close': 'destroy'
        },
        save: function (evt) {
            if (evt) { evt.preventDefault(); }
            this.model.save(this.getData()).done(_.bind(this.refreshLocations, this));
        },
        saveAsNew: function (evt) {
            if (evt) { evt.preventDefault(); }
            this.model.clear({silent: true});
            this.save(evt);
        },
        more: function (evt) {
            var $el = $(evt.target),
                menu;
            evt.preventDefault();
            menu = this.model.has('id') ? [
                {title: 'Save as new', cmd: _.bind(this.saveAsNew, this)}
            ] : [];
            menu.push({title: 'Close', cmd: _.bind(this.destroy, this)});
            (new ContextMenu({
                el: $el,
                menu: menu
            })).execute();
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
