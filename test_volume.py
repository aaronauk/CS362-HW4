import unittest
import sys
import volume

class TestVolume(unittest.TestCase):
    def test1(self):
        self.assertEqual(volume.volume(5), 125)
    def test2(self):
        self.assertEqual(volume.volume(-4), -1)
    def test3(self):
        self.assertEqual(volume.volume("6"), -1)

if __name__ == '__main__':
    unittest.main()