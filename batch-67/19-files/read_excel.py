from excel import OpenExcel
f = OpenExcel('names_db.xls')
print f.read('A')
print f.read('B')
print "{} is a {}".format(f.read('A7'),f.read('B7'))