define([
    'backbone', 
    'marionette',
    'router',
    'controllers/main'
], function (Backbone, Marionette, Router, Controller) {
    'use strict';

    var app = new Marionette.Application();

    app.addRegions({
        main: '#main'
    });

    app.addInitializer(function (options) {
        console.log(['app', options]);

        app.router = new Router({
            controller: new Controller({region: app.main})
        });
        Backbone.history.start();
    });

    return app; 
});
