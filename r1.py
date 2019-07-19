import xlrd
import mysql.connector
import datetime

name = "Anand1989.xls"
book = xlrd.open_workbook(name)
worksheet = book.sheet_by_index(0)
name = name[0:9]

db = mysql.connector.connect (host="localhost", user = "root", passwd = "", db = "rainfall")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS "+name)
create = ("""CREATE TABLE Anand1989  (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, ET DOUBLE(8,2), EP DOUBLE(8,2), BSS DOUBLE(8,2), RF DOUBLE(8,2), WD DOUBLE(8,2), WD1 DOUBLE(8,2), WS DOUBLE(8,2), DT1 DOUBLE(8,2), WT1 DOUBLE(8,2), DT2 DOUBLE(8,2), WT2 DOUBLE(8,2), MAXT DOUBLE(8,2), MINT DOUBLE(8,2), RH11 DOUBLE(8,2), RH22 DOUBLE(8,2), VP11 DOUBLE(8,2), VP22 DOUBLE(8,2), CLOUDM DOUBLE(8,2), CLOUDE DOUBLE(8,2), SOIL1 DOUBLE(8,2), SOIL2 DOUBLE(8,2), SOIL3 DOUBLE(8,2), SOIL4 DOUBLE(8,2), SOIL5 DOUBLE(8,2), SOIL6 DOUBLE(8,2), MinTtest DOUBLE(8,2), MaxTtest1 DOUBLE(8,2), MaxTtest2 DOBLE(8,2) )"""


