import unittest
class Test(unittest.TestCase):
    def TestMinus(self):
        result=6-5
        hope=1
        self.assertEqual(result,hope)
    def TestDivide(self):
        result=8/2
        hope=3
        self.assertEqual(result,hope)

if __name__ == '__main__':
    unittest.main()
