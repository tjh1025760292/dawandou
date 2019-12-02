import unittest

from tset01.tudou.test008 import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        print("测试开始")
    def tearDown(self):
        print("测试结束")

    def test_add(self):
        c=Calculator(3,5)
        result=c.add()
        assert result==8,"加法错误"
    def test_sub(self):
        """测试减法"""
        c=Calculator(7,2)
        result=c.sub()
        assert result==5,"减法错误"
    def test_mul(self):
        "测试加法"
        c=Calculator(3,3)
        result=c.mul()
        assert result==10,"乘法运算失败"
    def test_div(self):
        c=Calculator(6,2)
        result=c.div()
        assert result==3,"除法运算失败"

if __name__=="__main__":
  suit=unittest.TestSuite()
  suit.addTest(TestCalculator("test_add"))
  suit.addTest(TestCalculator("test_mul"))
  suit.addTest(TestCalculator("test_div"))
  suit.addTest(TestCalculator("test_sub"))

  runner=unittest.TextTestRunner()
  runner.run(suit)

