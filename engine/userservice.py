from md5 import md5
from random import random


class EmailRegistered(Exception):
    pass


class LoginRegistered(Exception):
    pass

class UserNotFound(Exception):
    pass


class IncorrectPassword(Exception):
    pass


class UserService(object):
    _mdb = None
    users = None

    def __init__(self, mongodb):
        self._mdb = mongodb
        self.users = self._mdb.users

    def get_user_by_field(self, key, value=''):
        return self.users.find_one({key: value})

    def authenticate(self, email, password):
        password_hash = md5(password).hexdigest()
        return self.users.find_one({
            'email': email,
            'password_hash': password_hash,
            })

    def register(self, email, login, password):
        if self.users.find({'email': email}).count():
            raise EmailRegistered('Found matching user(s)')
        if self.users.find({'login': login}).count():
            raise LoginRegistered('Found matching user(s)')
        salt = md5('%f%f%f' % (random(), random(), random())).hexdigest()
        return self.users.insert({
            'email': email,
            'login': login,
            'password_hash': self.get_password_hash(password, salt),
            'password_salt': salt
            })

    def sign_in(self, email, password):
        user = self.users.find_one({'email': email})
        if not user:
            raise UserNotFound()
        pass_hash = self.get_password_hash(password, user['password_salt'])
        if pass_hash != user['password_hash']:
            raise IncorrectPassword()
        return user

    def get_password_hash(self, password, salt):
        return md5(md5(password).hexdigest() + salt).hexdigest()
