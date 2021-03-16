from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains #scrolling pages
from selenium.webdriver.support.ui import WebDriverWait   #explicit
import random ####form random integer
import names

driver = webdriver.Chrome(r"D:\New folder (2)\chromedriver.exe")

driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_intro")

driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(5)
row_count=len (driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
print("no of rows",row_count)