from unittest import TestCase
from md5 import md5
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, User, Player
from engine.user import UserService, AlreadyRegistered
from exc import InvalidLoginCredentials


class TestUserService(TestCase):
    salt = ''
    db = None
    service = None

    def setUp(self):
        db_engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(db_engine)
        Session = sessionmaker(bind=db_engine)
        self.db = Session()
        self.service = UserService(Session(), salt=self.salt)

    def tearDown(self):
        self.db.close()

    def test_sign_in_good(self):
        email = 't@t.com'
        login = 'test'
        password = 'abuabuabu'
        user = User(login, email, md5(password + self.salt).hexdigest())
        self.db.add(user)
        self.db.commit()
        actual = self.service.sign_in(email, password)
        self.assertEquals(actual['login'], login)
        self.assertEquals(actual['email'], email)
        actual = self.service.sign_in(login, password)
        self.assertEquals(actual['login'], login)
        self.assertEquals(actual['email'], email)

    def test_sign_in_bad(self):
        email = 't@t.com'
        login = 'test'
        password = 'abuabuabu'
        test_password = 'asdf'
        user = User(login, email, md5(password + self.salt).hexdigest())
        self.db.add(user)
        self.db.commit()
        self.assertRaises(InvalidLoginCredentials,
                          self.service.sign_in, email, test_password)
        self.assertRaises(InvalidLoginCredentials,
                          self.service.sign_in, login, test_password)

    def test_register(self):
        self.service.register(email='test2@gmail.com',
                              login='test2',
                              password='test'
                              )
        query = self.db.query(User).filter_by(login='test2')
        user = query.one()
        self.assertIsNotNone(user)
        user_count = self.db.query(User).filter_by(id=user.id).count()
        self.assertEquals(user_count, 1)
        player_count = self.db.query(Player).filter_by(user_id=user.id).count()
        self.assertEquals(player_count, 1)

    def test_register_unique(self):
        self.service.register(email='test2@gmail.com',
                              login='test2',
                              password='test'
                              )
        self.assertRaises(AlreadyRegistered, self.service.register,
                          email='test3@gmail.com',
                          login='test2',
                          password='test'
                          )
        self.assertRaises(AlreadyRegistered, self.service.register,
                          email='test2@gmail.com',
                          login='test3',
                          password='test'
                          )

    def test_get_password_hash(self):
        password = 'test123'
        actual = self.service.get_password_hash(password)
        self.assertEquals(actual, md5(password + self.salt).hexdigest())
