from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
print(driver.title)
locator=("id","su")
text=u"百度一下"
result1=EC.title_is("jiangjiang")
result2=EC.title_contains("百")
result3=EC.text_to_be_present_in_element(locator,text)
result4=EC.text_to_be_present_in_element_value(locator,text)
result5=WebDriverWait(driver,10).until(EC.text_to_be_present_in_element_value(locator,text))
result6=WebDriverWait(driver,10).until(EC.title_contains(u"百度"))
print(result1(driver))
print(result2(driver))
print(result3(driver))
print(result4(driver))
print(result5)
#此处返回的是数值，所以不用加driver
print(result6)