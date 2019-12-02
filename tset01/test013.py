from selenium import webdriver
import unittest
class BaiduPage():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def get(self):
        self.driver.get("www.baidu.com")
    def input_keys(self,a):
        self.driver.find_element_by_id("kw").send_keys(a)
    def click(self):
        self.driver.find_element_by_d("su").click()
    def test_input(self):
        self.get()
        self.driver.input_keys(u"上海")