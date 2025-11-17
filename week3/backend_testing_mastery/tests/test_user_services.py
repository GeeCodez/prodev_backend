# tests/test_user_service.py

import unittest
from app.user_services import UserService

class TestUserService(unittest.TestCase):
    """Unit tests for the UserService class"""

    def setUp(self):
        """Runs before every test"""
        self.service = UserService()

    def test_add_valid_user(self):
        """Test adding a valid user"""
        result = self.service.add_user("Gee", 25)
        self.assertTrue(result)
        self.assertIn("Gee", self.service.get_usernames())

    def test_add_user_with_invalid_username(self):
        """Test adding user with invalid username"""
        with self.assertRaises(ValueError):
            self.service.add_user("", 20)

    def test_add_underage_user(self):
        """Test adding user below age 18"""
        with self.assertRaises(ValueError):
            self.service.add_user("Junior", 16)

    def test_get_usernames_empty(self):
        """Test usernames list when no user is added"""
        self.assertEqual(self.service.get_usernames(), [])

    def test_find_existing_user(self):
        self.service.add_user("Gee", 25)
        result = self.service.find_user("Gee")
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Gee")
        self.assertEqual(result["age"], 25)

    def test_find_user_is_case_insensitive(self):
        self.service.add_user("Gee", 25)
        result = self.service.find_user("gee")
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Gee")

    def test_find_nonexistent_user_returns_none(self):
        self.service.add_user("Gee", 25)
        result = self.service.find_user("Alex")
        self.assertIsNone(result)
