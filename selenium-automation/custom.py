from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains #scrolling pages
from selenium.webdriver.support.ui import WebDriverWait   #explicit


driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("http://127.0.0.1:5000/loginUser")

driver.maximize_window()
driver.implicitly_wait(10)


userName=driver.find_element_by_name("username")
userName.send_keys("lauserone")
passWord=driver.find_element_by_name("password")
passWord.send_keys("qwerty1234")
driver.find_element_by_xpath("/html/body/div/form/div/div[7]/button/img").click() #login
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/button/img").click() #patients 



driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[3]").click() #patientclick 
time.sleep(4)

 ############################ custom test #################################################
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[3]/button[2]").click() # custom test

time.sleep(2)
driver.find_element_by_id("customTestid").click()

driver.find_element_by_id("Assessmentcustom1").click()
#assesment  
driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/form/div[1]/div[1]/div[1]/div/input").send_keys("45") #age
driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/form/div[1]/div[2]/div[1]/label[1]").click() #gender
driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/form/div[1]/div[1]/div[2]/div[1]/input").send_keys("50")#weight

#driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/form/div[1]/div[1]/div[2]/div[2]/select").click()
 
driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/form/div[1]/div[2]/div[2]/div[1]/input").send_keys("160") #height
driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/form/div[2]/span").click()

time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/form/div[2]/div/div/div/div[3]/button[2]").click()


##############################  start test   ####################################
n =int(input("enter no of test :  "))
for i in range(n):

    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div[4]/div[3]/button/img[1]").click()
    driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/div[1]/input").send_keys("test"+str(i+1))
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/div[3]/button").click()
    time.sleep(8)
    try:
        if (driver.find_element_by_xpath("/html/body/div[2]/div/div[2]").text== 'Error!!'):
            print("Error")
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/div/button").click()
            
            
                
    except:
        print("not found")
    
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/div[5]/div[3]/button").click()
    time.sleep(8)


time.sleep(6)

#############################evaluation page##################################
driver.find_element_by_xpath("/html/body/div/div[4]/div[4]/button/img[2]").click()

xp = ['/html/body/div/div[31`]/div[1]','/html/body/div/div[3]/div[2]','/html/body/div/div[3]/div[3]','/html/body/div/div[3]/div[4]','/html/body/div/div[3]/div[5]','/html/body/div/div[3]/div[6]']
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
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[6]/div[4]/div/div/div/div[3]/button[2]").click()

###########################report generation##################################
time.sleep(3)
driver.find_element_by_xpath("/html/body/div/div[4]/div[5]/button/img").click


















'''
driver.find_element_by_xpath("/html/body/div[2]/div[1]/button/img").click()
driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/button/img[1]").click()
time.sleep(5)

#driver.close()


#driver.quit()
#/html/body/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[3]/button[2]

#/html/body/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[3]/button[1]

#/html/body/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[3]/button[3]
#username= input("Enter the username\n")
#driver.find_element_by_id("user-entry").send_keys(username)
#password= input("enter pasword\n")
#driver.find_element_by_id ("exampleFormControlInput1").send_keys(password)
#driver.find_element_by_xpath("/html/body/div/form/div/div[7]/button/img").click() 

'''