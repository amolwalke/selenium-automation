from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   #explicit


driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("https://secure.indeed.com/account/login")

driver.maximize_window()


time.sleep(5)

driver.find_element_by_id("login-email-input").send_keys("walkea4@gmail.com")
driver.find_element_by_id("login-password-input").send_keys("Amol1400@")
driver.find_element_by_id("login-submit-button").click()
time.sleep(10)
driver.find_element_by_class_name("gnav-header-1amsz23 e37uo190").click() 
time.sleep(7)
driver.find_element_by_xpath("/html/body/div/div[2]/span/div[3]/div[1]/div/div/div/form/div[1]/div[1]/div/div[2]/input").send_keys("software testing")
driver.find_element_by_xpath("/html/body/div/div[2]/span/div[3]/div[1]/div/div/form/div/div[1]/div/div[1]/div/div[2]/input").send_keys("software testing")
a=['Mumbai','Pune']
for x in a:

    try:

        driver.find_element_by_xpath("/html/body/div/div[2]/span/div[3]/div[1]/div/div/div/form/div[2]/div[1]/div/div[2]/input").send_keys(x)
        driver.find_element_by_xpath("/html/body/div/div[2]/span/div[3]/div[1]/div/div/div/form/div[3]/button").click()
        # driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td/div/div[2]/div/div[1]/ul/li[2]/a").click()
        driver.find_element_xpath("/html/body/table[1]/tbody/tr/td/div/div[2]/div/div[1]/ul/li[2]/a").click() #sorting 3days

        ###row count of openings
        row_count = len(driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div[5]/div/a"))
        print("no of rows",row_count)
        c = "/html/body/table[1]/tbody/tr/td/div/div[2]/div/div[1]/ul/li[2]/a"

    
        for i in range(row_count):
            print(F"{c}[{i+1}]")
            driver.find_elements_by_id("indeedApplyButton").click()
            driver.find_elements_by_id("resume-display-buttonHeader").click()
            driver.find_elements_by_xpath("/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
            driver.find_elements_by_xpath("/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
            driver.find_elements_by_xpath("/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
            driver.find_elements_by_xpath("/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]").click()
            driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
            driver.back()
            time.sleep(2)
            
    except:pass   

             
               





