import pandas as pd
import xlrd
import mysql.connector

# Open the workbook and define the worksheet
book = pd.read_excel("xyz.xlsx")
sheet = book.sheet_by_name("xyz")

# Establish a MySQL connection
database = mysql.connector.connect (host="localhost", user = "root", passwd = "", db = "mysqlpython")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO data (year,Min ,Max ,Mean, SD, CV, Skewness) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
		year		= sheet.cell(r,0).value
		Min	= sheet.cell(r,1).value
		Max			= sheet.cell(r,2).value
		Mean		= sheet.cell(r,3).value
		SD		= sheet.cell(r,4).value
		CV	= sheet.cell(r,5).value
		Skewness		= sheet.cell(r,6).value
		

		# Assign values from each row
		values = (year, Min, Max, Mean, SD, CV, Skewness)

		# Execute sql Query
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
columns = str(sheet.ncols)
rows = str(sheet.nrows)
#print("I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!")