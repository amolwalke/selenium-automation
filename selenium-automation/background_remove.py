from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   #explicit
import os
import pyautogui as ps
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("https://www.slazzer.com/")


driver.maximize_window()

path = "D:/Resized/"
dir_list = os.listdir(path)
leng= len(dir_list)
  
  
# print the list
print(leng)

for i in range(leng):
    driver.implicitly_wait(10)
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/section[1]/div/div[1]/div[2]/div/div[2]/button/span[1]'))).click()
    time.sleep(2)
    driver.find_elemnent_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div/div/button/span[1]").send_keys("D:/Resized/1-1.jpg \n D:/Resized/2-1.jpg")
    # button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[1]/div/div/button/span[1]')))
    # # q.send_keys("D:/Resized/{dir_list}.jpg")
    # for j in dir_list:
    #     q.send_keys(os.getcwd()+F"D:/Resized/{dir_list}.jpg")
    
