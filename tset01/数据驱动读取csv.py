import csv
import codecs
from itertools import islice
path=r"C:\Users\土豆\Desktop\data_move_readcsv.csv"
data=csv.reader(codecs.open(path,"r","gbk"))
users=[]
'''for i in islice(data,1,None):
    users.append(i)'''
for i in data:
    users.append(i[2])
print(users)