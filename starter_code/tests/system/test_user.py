from http import client

from models.user import UserModel
from test.base_test import BaseTest
import json

class UserTest(BaseTest):
    def test_register_user(self):
        with self.client:
            with self.app_context():
                request =client.post('/register', data={'username': 'test', 'password': "1234" })

                self.assertEqual(request.status_code, 201)
                self.asserIsNotNone(UserModel.find_by_username(username='test'))
                self.assertDictEqual({'message': 'User created successfully.'},
                                     json.loads(request.data))

    def test_login_user(self):
        pass

    def test_register_deuplciate_user(self):
        pass
