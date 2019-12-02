from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import  time
driver=webdriver.Chrome()
driver.get("file:///C:/Users/%E5%9C%9F%E8%B1%86/Desktop/%E6%96%B0%E5%BB%BA%E6%96%87%E6%9C%AC%E6%96%87%E6%A1%A3%20(8).html")
'''mouse=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
driver.implicitly_wait(4)
#s=driver.find_element_by_xpath("//*[id='nr']/option[1]").click()
m=driver.find_element_by_xpath("//*[@id='nr']")
#添加悬停，否则定位不到
#ActionChains(driver).move_to_element(mouse).perform()
Select(m).select_by_index(1)'''
m=driver.find_elements_by_xpath("//*[@type='checkbox']")
for i in m:
    i.click()
driver.implicitly_wait(2)
r=driver.find_element_by_id('c1').is_selected()
print(r)
#m=driver.switch_to_alert()
#m.accept()
ActionChains(driver).click_and_hold("target").perform()
ActionChains(driver).move_by_offset(2,0)

