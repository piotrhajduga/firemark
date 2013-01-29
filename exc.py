class FiremarkException(Exception):
    errno = 10


class NotLoggedIn(UserWarning, FiremarkException):
    errno = 11


class InsufficientPriviledges(UserWarning):
    errno = 18


class PlayerNotInLocation(Exception):
    errno = 16


class LocationNotFound(Exception):
    errno = 17
