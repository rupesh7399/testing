import pandas as pd
import xlrd
import mysql.connector

# Open the workbook and define the worksheet
name= "Anand1989.xls"
book = xlrd.open_workbook(name)
worksheet = book.sheet_by_index(0)

# Establish a MySQL connection
database = mysql.connector.connect (host="localhost", user = "root", passwd = "", db = "rainfall")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()
# cursor.execute("DROPE IF EXISTS"+name)
#Create table for insert data in database
# create = """CREATE TABLE"""+ name +"""(
#     id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
#     date DATE,
#     ET DOUBLE(8,2),
#     EP DOUBLE(8,2),
#     BSS DOUBLE(8,2),
#     RF DOUBLE(8,2),
#     WD DOUBLE(8,2),
#     WD1 DOUBLE(8,2),
#     WS DOUBLE(8,2),
#     DT1 DOUBLE(8,2),
#     WT1 DOUBLE(8,2),
#     DT2 DOUBLE(8,2),
#     WT2	DOUBLE(8,2),
#     MAXT DOUBLE(8,2),
#     MINT DOUBLE(8,2),
#     RH11 DOUBLE(8,2),
#     RH22 DOUBLE(8,2),
#     VP11 DOUBLE(8,2),
#     VP22 DOUBLE(8,2),
#     CLOUDM DOUBLE(8,2),
#     CLOUDE DOUBLE(8,2),
#     SOIL1 DOUBLE(8,2),
#     SOIL2 DOUBLE(8,2),
#     SOIL3 DOUBLE(8,2),
#     SOIL4 DOUBLE(8,2),
#     SOIL5 DOUBLE(8,2),
#     SOIL6 DOUBLE(8,2),
#     MinTtest DOUBLE(8,2),
#     MaxTtest1 DOUBLE(8,2),
#     MaxTtest2 DOUBLE(8,2),
#     )"""

# cursor.execute(create)
# Create the INSERT INTO sql query
query = """INSERT INTO  Anand1989(DATE,ET,EP,BSS,RF,WD,	WD1,WS,	DT1,WT1,DT2,WT2,MAXT,MINT,RH11,RH22,VP11,VP22,CLOUDM,CLOUDE,SOIL1,SOIL2,SOIL3,SOIL4,SOIL5,SOIL6,MinTtest,MaxTtest1,MaxTtest2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""


total_rows = worksheet.nrows
total_cols = worksheet.ncols
for r in range(1, worksheet.nrows):
    DATE      = worksheet.cell(r,0).value
    ET        = worksheet.cell(r,1).value
    EP        = worksheet.cell(r,2).value
    BSS       = worksheet.cell(r,3).value
    RF        = worksheet.cell(r,4).value
    WD        = worksheet.cell(r,5).value
    WD1       = worksheet.cell(r,6).value
    WS        = worksheet.cell(r,7).value
    DT1       = worksheet.cell(r,8).value
    WT1       = worksheet.cell(r,9).value
    DT2       = worksheet.cell(r,10).value
    WT2       = worksheet.cell(r,11).value
    MAXT      = worksheet.cell(r,12).value
    MINT      = worksheet.cell(r,13).value
    RH11      = worksheet.cell(r,14).value
    RH22      = worksheet.cell(r,15).value
    VP11      = worksheet.cell(r,16).value
    VP22      = worksheet.cell(r,17).value
    CLOUDM    = worksheet.cell(r,18).value
    CLOUDE    = worksheet.cell(r,19).value
    SOIL1     = worksheet.cell(r,20).value
    SOIL2     = worksheet.cell(r,21).value
    SOIL3     = worksheet.cell(r,22).value
    SOIL4     = worksheet.cell(r,23).value
    SOIL5     = worksheet.cell(r,24).value
    SOIL6     = worksheet.cell(r,25).value
    MinTtest  = worksheet.cell(r,26).value
    MaxTtest1 = worksheet.cell(r,27).value
    MaxTtest2 = worksheet.cell(r,28).value
    values = (DATE,ET,EP,BSS,RF,WD,WD1,WS,DT1,WT1,DT2,WT2,MAXT,MINT,RH11,RH22,VP11,VP22,CLOUDM,CLOUDE,SOIL1,SOIL2,SOIL3,SOIL4,SOIL5,SOIL6,MinTtest,MaxTtest1,MaxTtest2)
    cursor.execute(query, values)
        
# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print("") 
print ("All Done! Bye, for now.")
print ("")
# columns = str(sheet.ncols)
# rows = str(sheet.nrows)
# print("I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!")