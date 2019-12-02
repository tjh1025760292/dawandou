from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
url="https://www.baidu.com/"
driver.get(url)
WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("kw").send_keys("hao"))
