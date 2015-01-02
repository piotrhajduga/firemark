define([
    'underscore',
    'jquery',
    'marionette'
], function (_, $, Marionette) {
    'use strict';

    return Marionette.Controller.extend({
        initialize: function (options) {
            this.$el = $(Marionette.getOption(this, 'el'));
            this.$menu = this.buildMenu(Marionette.getOption(this, 'menu'));
            this.dfd = $.Deferred();
        },
        buildMenu: function (menu) {
            var self = this,
                $el = $('<ul/>'),
                $item,
                command;
            _.each(menu, function (item) {
                if (_.isArray(item.submenu)) {
                    $el.append(self.buildMenu(item.submenu));
                } else if (item.title && item.cmd) {
                    $item = $(_.template('<li><a href="#"><%= obj.title %></a></li>', item));
                    //$('body').one('click', _.bind(self.close, self));
                    $('a', $item).one('click', function (evt) {
                        evt.preventDefault();
                        self.select(item);
                    });
                    $item.appendTo($el);
                }
            });
            return $el;
        },
        execute: function () {
            this.$el.after(this.$menu.focus().blur(_.bind(function () {
                this.close();
            }, this)));
            return this.dfd.promise();
        },
        select: function (item) {
            var command = _.isString(item.cmd) ? Marionette.getOption(this, item.cmd) : item.cmd;
            if (_.isFunction(command)) {
                command.call(this);
                this.dfd.resolve();
            } else {
                this.dfd.reject();
            }
        },
        close: function () {
            this.$menu.remove();
        }
    });
});
