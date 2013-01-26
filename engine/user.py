from md5 import md5
from model import User, Player
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


class AlreadyRegistered(Exception):
    pass


class UserService(object):
    db = None

    def __init__(self, db, salt):
        self.db = db
        self.salt = salt

    def register(self, email, login, password):
        try:
            user_count = self.db.query(User).count()
            user = User(login, email, self.get_password_hash(password))
            if user_count == 0:
                user.add_role('builder')
            self.db.add(user)
            self.db.commit()
            player = Player()
            player.user_id = user.user_id
            self.db.add(player)
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise AlreadyRegistered()

    def sign_in(self, login, password):
        try:
            query = self.db.query(User)
            query = query.filter(or_(User.email == login, User.login == login))
            query = query.filter(User.password == self.get_password_hash(password))
            return query.one()
        except NoResultFound:
            return None

    def get_password_hash(self, password):
        return md5(password + self.salt).hexdigest()
