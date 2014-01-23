define([
    'underscore',
    'marionette',
    'models/create-mode/locations',
    'text!templates/create-mode/editor/exits.html'
], function (_, Marionette, Locations, tpl) {
    'use strict';

    return Marionette.ItemView.extend({
        template: _.template(tpl),
        initialize: function (options) {
            this.exits = options.exits || [];
            this.locations = new Locations();
        },
        serializeData: function () {
            return {
                exits: this.exits,
                locations: this.locations.toJSON()
            };
        },
        events: {
            'click .t-add-exit': 'addExit',
            'click .t-delete-exit': 'deleteExit'
        },
        ui: {
            location: '.f-location'
        },
        addExit: function (evt) {
            evt.preventDefault();
            var val = this.ui.location.val();
            console.log('exits.addExit');
            if (!_.findWhere(this.exits, {location: val})) {
                this.exits.push({
                    id: _.uniqueId(),
                    location: val
                });
                this.render();
            }
        },
        deleteExit: function (evt) {
            evt.preventDefault();
            var row = $(evt.target).closest('tr'),
                tdId = row.find('td').first().text();
            console.log('exits.deleteExit', tdId);
            this.exits = _.reject(
                this.exits,
                function (item) {
                    return item.id+'' === tdId.trim();
                }
            );
            this.render();
        },
        getData: function () {
            return this.exits;
        },
        onBeforeRender: function () {
            this.locations.fetch();
        }
    });
});
