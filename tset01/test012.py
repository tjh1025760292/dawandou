import unittest
from HTMLTestRunner import  HTMLTestRunner
import time
test_dir="./jisuanqi"
suit=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__=="__main__":
    add_title=time.strftime("%Y-%m-%d")
    fp=open('./test_report'+add_title+'2.html','wb')

    runner=HTMLTestRunner(stream=fp,title="计算器测试",description="运行环境：win10")
    runner.run(suit)