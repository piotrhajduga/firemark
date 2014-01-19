define(['underscore'], function (_) {
    function ErrorBuilder(options) {
        this.errors = [];
        this.options = options;
    }

    _.extend(ErrorBuilder.prototype, {
        getOption: function (name) {
            if (_.has(this.options, name)) {
                return this.options[name];
            }
            if (_.has(this, name)) {
                return this[name];
            }
        },
        validate: function (obj) {
            _.each(this.getOption('validators'), this._validate, this);
        },
        _validate: function (validator) {
            if (validator.check(obj)) { this.errors.push(validator.message); }
        },
        isEmpty: function () {
            return _.isEmpty(this.errors);
        }
    });

    return ErrorBuilder;
});
