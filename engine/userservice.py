from md5 import md5


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
        return self.users.insert({
            'email': email,
            'login': login,
            'password_hash': md5(password).hexdigest(),
            })
