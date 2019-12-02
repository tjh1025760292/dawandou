import unittest
'''test_dir="./tudou"
suits=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__=="__main__":
    runner=unittest.TextTestRunner()
    runner.run(suits)'''

class Mytest(unittest.TestCase):
    @unittest.skip
    def test_skip(self):
        print("aaa")
    @unittest.skipIf(3>2,"条件为真跳过测试")
    def test_skip_if(self):
        print("bbb")
    @unittest.skipUnless(2>3,"条件为真执行测试")
    def test_skip_unless(self):
        print("ccc")
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(2,3)
     
     ''' @classmethod
    def tearDownClass(cls):
        cls.driver,quit()'''