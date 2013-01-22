from md5 import md5
from random import random
from model import User, Player
from config import password_salt
from sqlalchemy import or_


class UserService(object):
    db = None

    def __init__(self, db, salt):
        self.db = db
        self.salt = salt

    def register(self, email, login, password):
        user = User(login, email, self.get_password_hash(password))
        self.db.add(user)
        self.db.commit()
        player = Player()
        player.user_id = user.user_id
        self.db.add(player)
        self.db.commit()

    def sign_in(self, login, password):
        query = self.db.query(User)
        query = query.filter(or_(User.email == login, User.login == login))
        query = query.filter(User.password == self.get_password_hash(password))
        return query.one()

    def get_password_hash(self, password):
        return md5(password + self.salt).hexdigest()
