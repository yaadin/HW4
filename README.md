!RUN TESTS FROM ROOT FOLDER AS MODULES NOT FILES (e.g python -m hw4.tests.userUtilTestclear or python -m hw4.tests.userTest or python -m hw4.tests.userServiceTest)!

This project creates a simple system to manage users. It includes classes that handle user information, operations, and helper functions.
The User class holds details about a user like their user_id, name, surname, email, password, and birthday. It also has methods to get the user’s details and calculate their 
age based on their birthday.

The UserService class manages users in the system. It has methods to add, find, delete, and update user details. It also has a method to count how many users are in the system.
The users are stored in a dictionary with their user_id as the key.

The UserUtil class has helpful methods for creating user IDs, generating strong passwords, checking if passwords are secure, creating email addresses, and validating email formats. 
It generates a unique user ID based on the current year and a random 7-digit number. The password generator makes sure the password has at least one lowercase letter, one uppercase 
letter, one number, and one special character. The email generator creates an email using the user’s name and surname. The email validation method checks if the email is correctly 
formatted.

This system makes it easy to create, update, and manage users while ensuring data is handled securely and correctly.
