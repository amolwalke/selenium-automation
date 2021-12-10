from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   #explicit
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("https://www.naukri.com/")

driver.maximize_window()


time.sleep(5)

driver.find_element_by_id("login_Layer").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/form/div[2]/input").send_keys("walkea4@gmail.com")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/form/div[3]/input").send_keys("amol1400")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/form/div[6]/button").click()
driver.implicitly_wait(10)

time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div/ul[1]/li[1]/a").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[1]/div[1]/form/div[1]/div/div[1]/div[1]/div[2]/input").send_keys("software testing")
driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[1]/div[1]/form/div[1]/div/div[2]/div[1]/div[2]/input").send_keys("Mumbai")
driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[1]/div[1]/form/div[1]/button").click()
row_count = len(driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[2]/section[2]/div[2]/article"))
print("no of rows",row_count)
for i in range(row_count):

    driver.find_element_by_xpath(F"/html/body/div[1]/div[3]/div[2]/section[2]/div[2]/article[{i+1}]/div[1]").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(5)
  
    driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[3]/div/button[2]").click()
    time.sleep(5)
    driver.close()
    driver.switch_to.window(driver.window_handles[1])
        
        





