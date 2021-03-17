from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains #scrolling pages
from selenium.webdriver.support.ui import WebDriverWait   #explicit

driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("https://www.makemytrip.com/flights/?cmp=SEM|D|DF|G|Brand|B_M_Makemytrip_Search_Exact|Brand_Top_5_Exact|Expanded|456320328647&s_kwcid=AL!1631!3!456320328647!e!!g!!makemytrip&ef_id=Cj0KCQjwrsGCBhD1ARIsALILBYqd6N4XkWIDSrg1cAw0QuRr6HeFeFGbWxKicWHkUwlpMK7Pva8NRnUaAraPEALw_wcB:G:s&gclid=Cj0KCQjwrsGCBhD1ARIsALILBYqd6N4XkWIDSrg1cAw0QuRr6HeFeFGbWxKicWHkUwlpMK7Pva8NRnUaAraPEALw_wcB")

driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div/div/nav/ul/li[2]/a").click()
a=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/input").click()
a.send_keys("Old Trafford Stadium, Manchester")
