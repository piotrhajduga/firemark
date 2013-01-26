from unittest import TestCase
from md5 import md5
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, User, Player
from engine.user import UserService, AlreadyRegistered


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
        self.service.register('test1', 'test1@test.com', 'bandooo')
        actual = self.service.sign_in('test1@test.com', 'bandooo')
        self.assertTrue(actual)
        actual = self.service.sign_in('test1', 'bandooo')
        self.assertTrue(actual)

    def test_sign_in_bad(self):
        self.service.register('test1', 'test1@test.com', 'bandooo')
        actual = self.service.sign_in('test1', 'asd')
        self.assertFalse(actual)
        actual = self.service.sign_in('test1@test.com', 'ha')
        self.assertFalse(actual)

    def test_register(self):
        self.service.register(
                email='test2@gmail.com',
                login='test2',
                password='test'
            )
        query = self.db.query(User).filter(User.login == 'test2')
        user = query.one()
        self.assertIsNotNone(user)
        query = self.db.query(Player).filter(Player.user_id == user.user_id)
        player = query.one()
        self.assertIsNotNone(player)

    def test_register_unique(self):
        self.service.register(
                email='test2@gmail.com',
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
