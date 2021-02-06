import unittest
import sys
import average_elements

class TestAverageOfElements(unittest.TestCase):
    def test1(self):
        self.assertEqual(average_elements.averageElements([2,4,6,8,10]), 6)
    def test2(self):
        self.assertEqual(average_elements.averageElements("20"), None)
    def test3(self):
        self.assertEqual(average_elements.averageElements([]), None)


if __name__ == '__main__':
    unittest.main()