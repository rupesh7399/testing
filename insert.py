import xlrd
import mysql.connector

# Open the workbook and define the worksheet
book = xlrd.open_workbook("xyz.xlsx")
worksheet = book.sheet_by_index(0)

# Establish a MySQL connection
database = mysql.connector.connect (host="localhost", user = "root", passwd = "", db = "mysqlPython")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO data (year, Min, Max, Mean, SD, CV, Skewness ) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
# for x in range(total_rows):
#     for y in range(total_cols):
#         record.append(worksheet.cell(x,y).value)
#     table.append(record)
#     record = []
#     x +=1
total_rows = worksheet.nrows
total_cols = worksheet.ncols
for r in range(1, worksheet.nrows):
    year    = worksheet.cell(r,0).value
    Min   =  worksheet.cell(r,1).value
    Max     =  worksheet.cell(r,2).value
    Mean    =  worksheet.cell(r,3).value
    SD      =  worksheet.cell(r,4).value
    CV      = worksheet.cell(r,5).value
    Skewness= worksheet.cell(r,6).value
    values = (year, Min, Max, Mean, SD, CV, Skewness)
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