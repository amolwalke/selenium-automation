from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   #explicit


driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("https://www.amazon.in/")

driver.maximize_window()


time.sleep(5)

driver.implicitly_wait(10)

driver.find_element_by_id("twotabsearchtextbox").send_keys("mechanical keyboard")
driver.find_element_by_id("nav-search-submit-button").click()
driver.find_element_by_xpath("//div[@class='a-section aok-relative s-image-fixed-height']/img[@data-image-index='5']").click()

driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_id("submit.add-to-cart").click()

driver.find_element_by_id("nav-cart-count-container").click()
driver.find_element_by_id("sc-buy-box-ptc-button").click()

driver.find_element_by_id("ap_email").send_keys("9137533244")
driver.find_element_by_id("continue").click()
time.sleep(4)
driver.find_element_by_id("ap_password").send_keys("amol1400")
driver.find_element_by_id("signInSubmit").click()
driver.find_element_by_xpath("//span[@class='a-button-inner']/a[@data-action='page-spinner-show']").click()

driver.find_element_by_xpath("//span[@class='a-button-inner']/input[@type='submit']").click()


driver.find_elements_by_xpath("//div[@id=pp-eGJjX7-138]/div[@class='a-box pmts-instrument-box']/div[@class='a-box-inner a-padding-small']/div[@class='a-fixed-left-grid']/div[@class='a-fixed-left-grid-inner']/div[@class='a-fixed-left-grid-col a-col-left']").click()