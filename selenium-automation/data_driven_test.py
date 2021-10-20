import time

import openpyxl
import xlutils
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")


driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
driver.implicitly_wait(10)

#path of excel sheet
path ='C:\\Users\\Amol\\Documents\\datadrivensheet.xlsx'

df = pd.read_excel(path)
usernames = df.iloc[:,0]
passwords = df.iloc[:,1]

# print(usernames,'\n',passwords)

for i in range(len(usernames)):
    if usernames[i] and passwords[i]:
        print(usernames[i],passwords[i])
        time.sleep(5)

        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input").send_keys(usernames[i])
    
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/input").send_keys(passwords[i])

      
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input").click()
        if driver.title == "Login: Mercury Tours":
            print("test case passed")
            driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]").click()
        

        else :
            print("test case failed")














