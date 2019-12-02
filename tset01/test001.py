#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(3)
#driver.get("http://idea.lanyus.com/")
#driver.close()
#time.sleep(3)
#driver.set_window_size(540,960)
#time.sleep(3)
#driver.find_element_by_id("kw").send_keys(u"顾城文")
#driver.find_element_by_id("su").click()
#driver.maximize_window()
#driver.get_screenshot_as_file("C:/Users/土豆/Desktop/mui.jpg")
#driver.find_element_by_tag_name("input").send_keys("hello")
#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[2]").click()
#driver.find_element_by_xpath('//*[@id="kw"]').send_keys(u"唐杰海")
#driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"V")
qq=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[7]")
ActionChains(driver).context_click(qq).perform()
#time.sleep(2)
#driver.find_element_by_id("kw").clear()
time.sleep(3)
driver.quit()