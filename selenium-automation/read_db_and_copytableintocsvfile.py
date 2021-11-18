import sqlite3
from openpyxl.workbook import Workbook
import pandas



con = sqlite3.connect(r'C:\\Users\\Amol\\.ohm3000KYA\\structuredData\\devicemanager.db')

cur = con.cursor()
outfile = open("D://databaase//out.csv", "w")

def dashboard_patient():
    for row in cur.execute('SELECT * FROM dashboard_kya_calculations'):
        print(row)
        for j in row:
            outfile.write(str(j) + ",")
        outfile.write("\n")
        pass

dashboard_patient()


def dashboard_customer_resgistration():
    outfile = open("D://databaase//out1.csv", "w")
    for row1 in cur.execute('SELECT * FROM dashboard_customer_resgistration'):
        print(row1)
        for fsq in row1:
            outfile.write(str(fsq) + ",")
        outfile.write("\n")
        pass

dashboard_customer_resgistration()





 
