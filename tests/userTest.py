import unittest
from hw4.classes import User
from datetime import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Meder", "Rakhatbekov", "rakhatbbekov@gmail.com", "salam", "08/2003")

    def test_get_details(self):
        expected_info = "user Meder Rakhatbekov with email: rakhatbbekov@gmail.com"
        self.assertEqual(self.user.get_details(), expected_info)

    def test_get_age(self):
        self.assertEqual(self.user.get_age(), 21)


if __name__ == "__main__":
    unittest.main()
