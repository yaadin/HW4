import unittest
from ..classes import User, UserService,UserUtil
from datetime import datetime
import string


class TestUserUtil(unittest.TestCase):
    def setUp(self):
        UserService.users = {}
        self.user1 = User(UserUtil.generate_user_id(), 'meder', 'peder','k','k','k')
        self.user2 = User(UserUtil.generate_user_id(), 'ggg', 'canelo','k','k','k')
        self.user3 = User(UserUtil.generate_user_id(), 'salam', 'world','k','k','k')
        UserService.add_user(self.user1)
        UserService.add_user(self.user2)
        UserService.add_user(self.user3)

    def test_generate_user_id(self):
        self.assertIsInstance(self.user1.user_id, str) 
        self.assertEqual(len(self.user1.user_id), 9)  
        

    def test_generate_password(self):
        self.user1.password = UserUtil.generate_password(10)  
        self.user2.password = UserUtil.generate_password()  
        self.user3.password = UserUtil.generate_password(12)  

        for person in UserService.users.values():
            self.assertGreaterEqual(len(person.password), 8, "less than 8")  

        for person in UserService.users.values():  
            password = person.password
            self.assertTrue(any(char.islower() for char in password), "No lowercase letter")
            self.assertTrue(any(char.isupper() for char in password), "No uppercase letter")
            self.assertTrue(any(char.isdigit() for char in password), "No digit")
            self.assertTrue(any(char in string.punctuation for char in password), "No special character")

        self.assertEqual(len(self.user1.password), 10)
        self.assertEqual(len(self.user2.password), 8)

    def test_is_strong_password(self):
        self.assertTrue(UserUtil.is_strong_password("1Kyrgyzstan@12"))  
        self.assertFalse(UserUtil.is_strong_password("heheh08"))  

    def test_genearte_email(self):
        self.assertEqual(UserUtil.generate_email('Meder', 'Rakhatbekov'), 'meder.rakhatbekov@gmail.com')

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("meder.rakhatbbekov@gmail.com"))
        self.assertFalse(UserUtil.validate_email("rakhatbbekov@gmail.com"))  

if __name__ == "__main__":
    unittest.main()