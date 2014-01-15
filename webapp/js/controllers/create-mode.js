define([
    'marionette',
    'app',
    'views/create-mode/content'
], function (Marionette, App, CreateModeView) {
    return Marionette.Controller.extend({
        createMode: function () {
            App.main.show(new CreateModeView());
        },
        gameMode: function () {
            App.main.close();
        }
    });
});
