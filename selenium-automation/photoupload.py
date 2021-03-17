from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains #scrolling pages
from selenium.webdriver.support.ui import WebDriverWait   #explicit
import random ####form random integer
import names

driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("https://www.myheritage.com/deep-nostalgia")

driver.maximize_window()
driver.implicitly_wait(10)


q=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div/div/div/div/div[1]/div[2]/section/div[1]/div[1]/button/span/input")
q.send_keys("D:\chromdriver\download.jpg")
