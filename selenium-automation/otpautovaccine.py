from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains #scrolling pages
from selenium.webdriver.support.ui import WebDriverWait   #explicit
from selenium.webdriver.common.keys import Keys
import pyautogui as ps
import pyperclip

driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("https://selfregistration.cowin.gov.in/")

driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(5)

driver.find_element_by_id("mat-input-0").send_keys("9137533244")
driver.execute_script("window.open('','_blank');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://web.airdroid.com/")
ps.click(x=1319, y=906)



time.sleep(2)
q = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[18]/div[2]/div/div[3]/div[1]/div[1]/div[1]/div[1]/input")
q.send_keys("walkea61@gmail.com")
p = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[18]/div[2]/div/div[3]/div[1]/div[1]/div[1]/div[2]/input")
p.send_keys("amol1400")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[18]/div[2]/div/div[3]/div[1]/div[1]/div[1]/div[2]/button").click()

time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[23]/div[2]/div/div[3]/button").click()

ps.click(x=69, y=437)

driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.find_element_by_xpath("/html/ body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button").click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
time.sleep(8)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[23]/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div[1]/div[1]/div/div[1]/div[1]").click()


content = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div[23]/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[2]/div/div[1]/div[18]/div/div[1]/div[1]")[0].text

ps.doubleClick(x=1214, y=598)

ps.hotkey('ctrl', 'c')
driver.switch_to.window(driver.window_handles[0])
u = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[2]/ion-item/mat-form-field/div/div[1]/div/input").click()
ps.hotkey('ctrl', 'v')
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[3]").click()



