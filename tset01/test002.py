from selenium import webdriver
import time
import random
"""driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(5)
f=driver.current_window_handle
driver.get("https://blog.csdn.net/u014801403/article/details/79085085")
time.sleep(3)
all=driver.window_handles
for i in all:
    if not i==f:
        driver.switch_to(i)
m=driver.current_window_handle
s=driver.title
print(s)"""
driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys(u"上海")
driver.find_element_by_id("su").click()
time.sleep(5)
m=driver.find_elements_by_xpath("//h3/a")
x=random.randint(0,8)
z=0
#t=m[x].get_attribute("href")
m[x].click()
#print(t)
#driver.get(t)
time.sleep(3)
"""for i in m:
    print (i.get_attribute("href"))
    z+=1
    print(z)"""
driver.quit()