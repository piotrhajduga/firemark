Array.prototype.each = function(fun) {
    var i;
    for (i = 0; i < this.length; i++) {
        fun(this[i]);
    }
};
