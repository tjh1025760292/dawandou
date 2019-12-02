import unittest
class Testuse(unittest.TestCase):
    def test_equal(self):
        self.assertEqual("p","p")
        self.assertNotEqual("7","7")
    def test_in(self):
        self.assertIn("hello","hello world")
        self.assertNotIn("P","QQ")
    def taet_true(self):
        self.assertTrue(True)
        self.assertFalse(False)

if __name__=="__main__":
    unittest.main()