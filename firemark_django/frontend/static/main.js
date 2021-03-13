var $Main = $("#Main");

$.ajax({
    url: "/main",
    success: function (result) {
        $Main.html(result);
    },
    error: function () {
        $Main.html("sum ting wong");
    }
});
