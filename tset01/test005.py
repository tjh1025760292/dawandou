from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/%E5%9C%9F%E8%B1%86/Desktop/%E6%96%B0%E5%BB%BA%E6%96%87%E6%9C%AC%E6%96%87%E6%A1%A3%20(9).html")
t=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]")
print(t.text)
profile_directory=r"C:\Users\土豆\AppData\Roaming\Mozilla\Firefox\Profiles\0kd7c7hp.default"
profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)
t.get_attribute("id")