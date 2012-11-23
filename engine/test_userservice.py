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
        self.service.register(
                email='test2@gmail.com',
                login='test2',
                password='test'
                )
        actual = self.mdb.users.find(
                {'email': 'test2@gmail.com'},
                {'login': 'test2'}
                ).count()
        self.assertEquals(1, actual)

    def test_register_starting_location(self):
        self.service.register(
                email='test2@gmail.com',
                login='test2',
                password='test'
                )
        location = self.mdb.users.find_one({
            'email': 'test2@gmail.com',
            'login': 'test2',
            })['location_id']
        self.assertNotNone(location)
