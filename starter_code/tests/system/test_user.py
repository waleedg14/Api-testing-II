from http import client

from models.user import UserModel
from test.base_test import BaseTest
import json

class UserTest(BaseTest):
    def test_register_user(self):
        with self.client:
            with self.app_context():
                response =client.post('/register', data={'username': 'test', 'password': "1234" })

                self.assertEqual(response.status_code, 201)
                self.asserIsNotNone(UserModel.find_by_username(username='test'))
                self.assertDictEqual({'message': 'User created successfully.'},
                                     json.loads(response.data))

    def test_login_user(self):
        with self.client:
            client.post('/register', data={'username': 'test', 'password': "1234" })
            auth_response = client.post('/auth/login',
                                       data=json.dumps({'username': 'test', 'password': "1234" }),
                                       headers={'Content-Type': 'application/json'})
            self.assertIn('access_token', json.loads(auth_response.data).keys())

    def test_register_duplciate_user(self):
        with self.client:
            client.post('/register', data={'username': 'test', 'password': "1234"})
            response = client.post('/register', data={'username': 'test', 'password': "1234" })

            self.assertEqual(response.status_code, 400)
            self.assetDictEqual({'message': 'User created successfully.'},
                                json.loads(response.data))
