import unittest
from password_validator import is_password_secure

class TestPasswordValidation(unittest.TestCase):
    def test_password_length(self):
        self.assertFalse(is_password_secure("short"))

    def test_password_uppercase(self):
        self.assertFalse(is_password_secure("alllowercase1!"))

    def test_password_lowercase(self):
        self.assertFalse(is_password_secure("ALLUPPERCASE1!"))

    def test_password_digit(self):
        self.assertFalse(is_password_secure("NoDigits!"))

    def test_password_special_char(self):
        self.assertFalse(is_password_secure("NoSpecialChars1"))

    def test_valid_password(self):
        self.assertTrue(is_password_secure("P@ssw0rd!"))

if __name__ == '__main__':
    unittest.main()