'use strict';

require.config({
    baseUrl: 'js',
    paths: {
        underscore: 'vendor/underscore',
        jquery: 'vendor/jquery-1.8.0',
        backbone: 'vendor/backbone',
        marionette: 'vendor/backbone.marionette'
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

require(['jquery', 'app'], function ($, App) {
    $(function () {
        App.start();
    });
});
