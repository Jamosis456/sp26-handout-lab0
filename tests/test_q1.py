"""Tests for Lab 0 Question 1"""

import sys
sys.path.append(".")
import unittest
from src.q1 import is_palindrome
class TestPalindrome(unittest.TestCase):
    def test_simple_palindrome(self) -> None:
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome(self) -> None:
        self.assertFalse(is_palindrome("cowboy"))

    def test_ignore_case_and_symbols(self) -> None:
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama?"))

if __name__ == "__main__":
    unittest.main()
