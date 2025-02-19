from datetime import datetime
from datetime import datetime
from random import randint
import random, string

class User:
    def __init__(self, user_id : int, name : str, surname : str, email : str,password : str, birthday : str):
        self.user_id = user_id
        self.name = name 
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday

    def get_details(self):
        return f"user {self.name} {self.surname} with user id: {self.user_id}"
    def get_age(self):
        x = self.birthday.split('/')
        if datetime.now().month - int(x[0]) >= 0:
            return datetime.now().year - int(x[1])
        else:
            return datetime.now().year - int(x[1]) - 1
        
class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.id] = user 
    
    @classmethod
    def find_user(cls, user):
        cls.users.get(user.id, "Not found")

    @classmethod
    def delete_user(cls,user):
        cls.users.pop(user.id, "Not Found")

    @classmethod
    def update_user(cls, user_id, name = None, id = None, birthday = None, surname = None):
        if name:
            cls.users.get(user_id, "Not found").name = name
        if id:
             cls.users.get(user_id, "Not found").user_id = id
        if surname:
             cls.users.get(user_id, "Not found").surname = surname
        if birthday:
             cls.users.get(user_id, "Not found").birthday= birthday
    
    @classmethod
    def get_number(cls):
        return len(cls.users)
    

class UserUtil:
    @staticmethod
    def generate_user_id():
        year = str(datetime.now().year)
        num = f"{randint(1, 9999999):07d}"
        user_id = year[2:] + num
        if user_id in UserService.users.keys():
            num = f"{randint(1, 9999999):07d}"
            user_id = year[2:] + num
            return user_id
        else:
            return user_id

    @staticmethod
    def generate_password(length=8):
        if length < 8:
            raise ValueError("Length of password must be at least 8")

        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)]

        all_chars = string.ascii_letters + string.digits + string.punctuation
        password += (random.choices(all_chars, k=length - 4))
        random.shuffle(password)
        password = ''.join(password)
        return password

    @staticmethod
    def is_strong_password(password):
        uppercase = False
        lowercase = False
        number = False
        special_char = False

        for char in password:
            if char in string.ascii_uppercase:
                uppercase = True
            elif char in string.ascii_lowercase:
                lowercase = True
            elif char in string.digits:
                number = True
            elif char in string.punctuation:
                special_char = True

        return uppercase and lowercase and number and special_char

    @staticmethod
    def generate_email(name, surname, domain='gmail.com'):
        return f"{name.lower().replace(' ', '_')}.{surname.lower().replace(' ', '_')}@{domain}"

    @staticmethod
    def validate_email(email):
        if email.count('@') != 1:
            return False
        email_components = email.split('@')  

        if '.' not in email_components[0]:
            return False

        if '.' not in email_components[1]:
            return False

        part1 = email_components[0].split('.')
        part2 = email_components[1].split('.')

        if not part1[0].isalpha() or not part1[1].isalpha():
            return False

        if len(part2) < 2:
            return False

        if part2[-1] != 'com':
            return False

        return True









