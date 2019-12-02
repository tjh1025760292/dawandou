from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://mail.163.com/')
time.sleep(3)
'''#先于iframe找到父元素，且点击不可触及的页面
driver.find_element_by_xpath("//*[@id='lbNormal']").click()
#找到所有的iframe
m=driver.find_elements_by_tag_name("iframe")
#跳转到iframe的列表中多个的某一个，用序号
driver.switch_to_frame(m[0])'''
driver.find_element_by_xpath("//*[@id='lbNormal']").click()
m=driver.find_element_by_css_selector("iframe[id^='x-URS-iframe']")
driver.switch_to_frame(m)
driver.find_element_by_name("email").send_keys("123")
driver.find_element_by_name("password").send_keys("456")
driver.switch_to_default_content()
time.sleep(3)
driver.quit()



