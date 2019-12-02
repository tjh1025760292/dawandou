import xlrd
path=r"C:\Users\土豆\Desktop\数据驱动读取excel.xlsx"
data=xlrd.open_workbook(path)
print(data.sheet_by_index(0))
m=data.sheet_by_name(u"工作表1")
print(m.nrows)
print(m.ncols)
h=m.row_values(2)
print(h[3])