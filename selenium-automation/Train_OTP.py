from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains #scrolling pages
from selenium.webdriver.support.ui import WebDriverWait   #explicit
import random ####form random integer
import names
import pytesseract

from PIL import Image


driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("https://www.irctc.co.in/nget/train-search")

driver.maximize_window()
driver.implicitly_wait(20)


driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button").click()
driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]").click()
time.sleep(5)
otpimage = driver.find_element_by_xpath("/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div/app-nlp-captcha/div/div[2]/div/div[1]/a/img")
otpimage.get_screenshot_as_file(r"C:\Users\Amol\Desktop\New folder\home.png")

time.sleep(10)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


text_from_image = pytesseract.image_to_string(Image.open(r"C:\Users\Amol\Desktop\New folder\home.png"))

print(text_from_image)

