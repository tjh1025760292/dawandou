from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://news.baidu.com/")
time.sleep(2)
driver.set_window_size(800,600)
'''m=driver.page_source
print(m)'''
#滚动条到顶
js="var q=document.getElementById('id').scrollTop=0"
driver.execute_script(js)
time.sleep(3)
#滚动条到底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
js = "window.scrollTo(100,400);"
driver.execute_script(js)
#页面跳到元素也是js
target = driver.find_element_by_xxxx()
driver.execute_script("arguments[0].scrollIntoView();", target)
#谷歌浏览器横着拉起来
js = "var q=document.body.scrollTop=0"
driver.execute_script(js)

