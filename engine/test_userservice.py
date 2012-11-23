from unittest import TestCase
from pymongo import Connection
from md5 import md5
import userservice as usrs


class TestUserService(TestCase):
    mdb = Connection().unittests

    def setUp(self):
        self.service = usrs.UserService(self.mdb)

    def tearDown(self):
        self.mdb.users.drop()

    def test_get_user_by_field(self):
        self.mdb.users.insert({
            'email': 'kosarock@gmail.com',
            'login': 'kosa',
            'password_hash': md5('ukulele').hexdigest(),
            })
        actual = self.service.get_user_by_field('login', 'kosa')
        self.assertEquals('kosarock@gmail.com', actual['email'])
        self.assertEquals('kosa', actual['login'])
        self.assertEquals(md5('ukulele').hexdigest(), actual['password_hash'])
        actual = self.service.get_user_by_field('email', 'kosa')
        self.assertIs(None, actual)

    def test_authenticate(self):
        self.mdb.users.insert({
            'email': 'kosarock@gmail.com',
            'login': 'kosa',
            'password_hash': md5('ukulele').hexdigest(),
            })
        actual = self.service.authenticate('kosarock@gmail.com', 'ukulele')
        self.assertTrue(actual)
        actual = self.service.authenticate('kosarock@gmail.com', 'ha')
        self.assertFalse(actual)
        actual = self.service.authenticate('kosa', 'ukulele')
        self.assertFalse(actual)

    def test_register(self):
        uid = self.service.register(
                email='test2@gmail.com',
                login='test2',
                password='test'
                )
        self.assertIsNotNone(uid)
        actual = self.mdb.users.find_one({
            'email': 'test2@gmail.com',
            'login': 'test2',
            })
        self.assertIsNotNone(actual)

    def test_register_unique(self):
        self.mdb.users.insert({
            'email': 'test2@gmail.com',
            'login': 'test2',
            'password_hash': 'testtesttest'
            })
        self.assertRaises(usrs.UserExists, self.service.register,
                email='test2@gmail.com', login='test3', password='test')
        self.assertRaises(usrs.UserExists, self.service.register,
                email='test3@gmail.com', login='test2', password='test')

    def test_get_password_hash(self):
        password = 'test123'
        salt = 'salt123'
        actual = self.service.get_password_hash(password, salt)
        self.assertEquals(actual,
                md5(md5(password).hexdigest() + salt).hexdigest())

    def test_register_salted(self):
        password = 'test'
        uid = self.service.register(
                email='test2@gmail.com',
                login='test2',
                password=password
                )
        user = self.mdb.users.find_one({'_id': uid})
        self.assertIsNotNone(user['password_salt'])
        expected_hash = self.service.get_password_hash(
                password, user['password_salt'])
        self.assertEquals(user['password_hash'], expected_hash)

    def test_sign_in(self):
        self.mdb.users.insert({
            'email': 'test2@gmail.com',
            'login': 'test2',
            'password_hash': self.service.get_password_hash('test', 'salt'),
            'password_salt': 'salt',
            })
        user = self.service.sign_in(email='test2@gmail.com', password='test')
        self.assertIsNotNone(user)
        self.assertEquals(user['login'], 'test2')

    def test_sign_in_bad(self):
        self.mdb.users.insert({
            'email': 'test2@gmail.com',
            'login': 'test2',
            'password_hash': self.service.get_password_hash('test', 'salt'),
            'password_salt': 'salt',
            })
        self.assertRaises(usrs.IncorrectPassword, self.service.sign_in,
                email='test2@gmail.com', password='test2')
        self.assertRaises(usrs.UserNotFound, self.service.sign_in,
                email='notfound@gmail.com', password='test2')
