from xml.dom.minidom import parse
path=r"C:\Users\土豆\Desktop\数据驱动读取XML.XML"
data=parse(path)
root=data.documentElement
tagname=root.getElementsByTagName("item")
print(tagname[0].getAttribute("vid"))
print(tagname[1].getAttribute("size"))