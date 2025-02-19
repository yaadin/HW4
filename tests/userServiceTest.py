import unittest
from ..classes import UserService, User


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Meder", "Rakhatbekov", "rakhatbbekov@gmail.com", "qwerty", "08/2003")

    def test_add_user(self):
        UserService.add_user(self.user)
        self.assertIn(self.user, UserService.users.values())

    def test_find_user(self):
        UserService.add_user(self.user)
        self.assertIn(self.user.user_id, UserService.users)

    def test_delete_user(self):
        UserService.add_user(self.user)
        UserService.delete_user(self.user.user_id)
        self.assertNotIn(self.user.user_id, UserService.users)

    def test_get_number(self):
        UserService.users = {}
        user1 = User(1, 'k', 'k', 'email1@example.com', 'pass1', '01/01/1990')
        user2 = User(2, 'k', 'k', 'email2@example.com', 'pass2', '01/01/1990')
        user3 = User(3, 'k', 'k', 'email3@example.com', 'pass3', '01/01/1990')
        for user in (user1, user2, user3):
            UserService.add_user(user)

        expected_number = len(UserService.users)
        self.assertEqual(expected_number, UserService.get_number())

    def test_get_number(self):
        UserService.users = {}
        user1 = User(1, "salam", "worls", "salam@example.com", "password123", "01/01/2000")
        user2 = User(2, "kulity", "papulity", "kulity@example.com", "password456", "02/02/1995")
        user3 = User(3, "meder", "peder", "meder@example.com", "password789", "03/03/1990")
        for user in (user1, user2, user3):
            UserService.add_user(user)

        expected_users = [user1, user2, user3]
        self.assertEqual(len(expected_users), UserService.get_number())


if __name__ == "__main__":
    unittest.main()