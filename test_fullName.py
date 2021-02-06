import unittest
import sys
import fullName

class TestfullName(unittest.TestCase):
    def test1(self):
        self.assertEqual(fullName.fullName("Aaron", "Au"), "Aaron Au")
    def test2(self):
        self.assertEqual(fullName.fullName(6, "Au"), None)
    def test3(self):
        self.assertEqual(fullName.fullName("Aaron", ""), None)


if __name__ == '__main__':
    unittest.main()