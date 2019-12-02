import time
from selenium import webdriver
path=r"C:\Users\土豆\Desktop\数据驱动被读取txt.txt"
m=open(path,"r",1,"utf_8")
data=m.readlines()
users=[]
for i in data:
    user=i[:-1].split(":")
    users.append(user)
print(users)
