from models.user import UserModel
from test.unit.unit_base_test import UnitBaseTest

class TestUserModel(UnitBaseTest):
    def test_user_creation(self):
        user = UserModel('test', 'abcd')

        self.assertIsInstance(user.username, 'test' ,)
        self.assertIsInstance(user.password, 'abcd' ,)