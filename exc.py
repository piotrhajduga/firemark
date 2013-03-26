class FiremarkException(Exception):
    errno = 10
    msg = 'Application specific exception'

    def __str__(self):
        return 'Error %d: %s' % (self.errno, self.msg)

    def __repr__(self):
        if self.__class__ != FiremarkException:
            return '%s(%s)' % (
                self.__class__.__name__,
                FiremarkException.__name__
            )
        return repr(self)


class NotLoggedIn(FiremarkException):
    errno = 11
    msg = 'User not logged in'


class InvalidLoginCredentials(FiremarkException):
    errno = 12
    msg = 'Invalid login credentials'


class InsufficientPriviledges(FiremarkException):
    errno = 18
    msg = 'Insufficient priviledges'


class PlayerNotInLocation(FiremarkException):
    errno = 16
    msg = 'Player not in location'


class LocationNotFound(FiremarkException):
    errno = 17
    msg = 'Location not found'


class AlreadyRegistered(FiremarkException):
    errno = 19
    msg = 'User is already registered'
