from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   #explicit
from selenium.webdriver.common.action_chains import ActionChains #scrolling pages


driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("http://127.0.0.1:5000/CustomEvaluationPage")
driver.maximize_window()

#driver.execute_script("window.scrollBy(0,600)","")
time.sleep(5)

javaScript='function myFunction() {var person = prompt("Please enter your name:","");return person;};var n = myFunction();return n'
print(driver.execute_script(javaScript))
javaScript= ''
print(driver.execute_script(javaScript))





xp = ['/html/body/div/div[3]/div[1]','/html/body/div/div[3]/div[2]','/html/body/div/div[3]/div[3]','/html/body/div/div[3]/div[4]','/html/body/div/div[3]/div[5]','/html/body/div/div[3]/div[6]']
count=1
for i in xp:
    if count == n+1:
        break 
    target = driver.find_element_by_xpath(i)
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.perform()
    count=count+1
    time.sleep(5)

driver.find_element_by_xpath("/html/body/div/div[3]/div[6]/div[2]/div[1]/textarea").send_keys("pl")
driver.find_element_by_xpath("/html/body/div/div[3]/div[6]/div[2]/div[2]/textarea").send_keys("dia")
driver.find_element_by_xpath("/html/body/div/div[3]/div[6]/div[3]/div[1]/textarea").send_keys("tp")
driver.find_element_by_xpath("/html/body/div/div[3]/div[6]/div[3]/div[2]/textarea").send_keys("fu")
driver.find_element_by_xpath("/html/body/div/div[3]/div[6]/div[4]/button[1]").click()
time.sleep(5)

driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/div").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[6]/div[4]/button[2]").click()




