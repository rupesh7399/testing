#import the xlrd module
import xlrd

#Open the spreadsheet file(or workbook)
workbook = xlrd.open_workbook("xyz.xlsx")

#open a sheet:
#if you know the name of the sheet,you can open it by

#if you are not sure of the name of the sheet,
#you can open the first worksheet by it's index as folloqw:

worksheet = workbook.sheet_by_index(0)

#Once you have selected the worksheet,
#you can extract the value of a particular data cell as follows:
print("the value at row 4 and column 2 is : {0}".format(worksheet.cell(4,2).value))
#if you wants to know the number of sheets,
#use the property nsheets on the workbook object:
#print("the total number of sheet: {0}".format())
#if you want to have a list of the names of the sheets present in the file,
#use the function sheet_name() on the workbook object
sheets_name = workbook.sheet_names()
print("sheet names : {0}".format(sheets_name))

#to find the total number of rows and columns in the sheet use the property nrows and ncols with 
#the sheet object

total_rows = worksheet.nrows
total_cols = worksheet.ncols

print("number of rows : {0}, and number of columns : {1}".format(total_rows,total_cols))

#final tip';
#let's loop in every record in the worksheet and store them in a list then display the final list:
table = list()
record = list()

for x in range(total_rows):
    for y in range(total_cols):
        record.append(worksheet.cell(x,y).value)
    table.append(record)
    record = []
    x +=1

    print(table)