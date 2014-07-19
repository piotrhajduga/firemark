'use strict';

require.config({
    baseUrl: 'js',
    urlArgs: 'bust=' +  (new Date()).getTime(),
    paths: {
        underscore: 'vendor/underscore',
        jquery: 'vendor/jquery-1.8.0',
        backbone: 'vendor/backbone',
        marionette: 'vendor/backbone.marionette',
        'faux-server': 'vendor/backbone-faux-server',
        templates: '../templates'
    },
    //map: {
        //'*': {'jquery': 'vendor/jquery-private'},
        //'jquery-private': {'jquery': 'jquery'}
    //},
    shim: {
        jquery: {
            exports: 'jQuery'
        },
        underscore: {
            exports: '_'
        },
        backbone: {
            deps: ['jquery', 'underscore'],
            exports : 'Backbone'
        },
        marionette: {
            deps: ['jquery', 'underscore', 'backbone'],
            exports: 'Marionette'
        }
    }
});

require(['jquery', 'app', 'config'], function ($, app, config) {
    $(function () {
        if (config.useFauxServer) {
            require(['mocks/server']);
        }
        app.start();
    });
});
