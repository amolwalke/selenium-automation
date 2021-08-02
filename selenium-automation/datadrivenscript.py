
import xlrd

workbook =xlrd.open_workbook(r"C:\Users\Amol\Documents\Book1.xlsx")

sheet= workbook.sheet_by_name("Sheet1")


row_count = sheet.nrow
col_count= sheet.ncol
print(row_count)
print(col_count)

