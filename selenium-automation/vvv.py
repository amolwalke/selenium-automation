from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"D:\New folder (2)\chromedriver.exe")
driver.get("http://127.0.0.1:5000/loginUser")

driver.find_element_by_name("username").send_keys("lauserone")
driver.find_element_by_name("password").send_keys("qwerty1234")
driver.find_element_by_xpath("/html/body/div[1]/form/div/div[7]/button/img").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/button/img").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr[1]/td[3]").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[3]/button[3]").click()
time.sleep(5)

driver.implicitly_wait(10)

#########personal info############
driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/form/div[1]/div[1]/div[1]/div/input").send_keys("24")
driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/form/div[1]/div[2]/div[1]/label[2]").click()
driver.find_element_by_id("weight").send_keys("76")
#dropdown = Select(driver.find_element_by_id("weightunits"))
#dropdown.select_by_index(1)
#driver.find_element_by_id("weight").send_keys("76")



driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/form/div[1]/div[2]/div[2]/div[1]/input[1]").send_keys("157")
#dropdown = Select(driver.find_element_by_id("heightunits"))
#dropdown.select_by_index(1)
#driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/form/div[1]/div[2]/div[2]/div[1]/input[1]").click()
#driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/form/div[1]/div[2]/div[2]/div[1]/input[2]").send_keys("5")
#driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/form/div[1]/div[2]/div[2]/div[1]/input[3]").send_keys("10")



######save button#########

driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/form/div[2]/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[4]/form/div[2]/div/div/div/div[3]/button[2]").click()
time.sleep(2)


########Test################
driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[2]/div/select").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[2]/div/select").click()
dropdown = Select(driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[2]/div/select"))
dropdown.select_by_index(0)





driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[4]/div/select").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[4]/div/select").click()
dropdown = Select(driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[4]/div/select"))
dropdown.select_by_index(1)


#driver.find_element_by_xpath("/html/body/div/div[4]/div[3]/div[2]/button[1]/img").click()
time.sleep(1)
driver.find_element_by_id("start-btn").click()
time.sleep(8)


driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div/div/div[2]/button").click()



'''
###driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div/div/div[2]/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div/div/div/div/div[3]/button[2]").click()


########### 2nd Test########
driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[2]/div/select").click()
dropdown = Select(driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[2]/div/select"))
dropdown.select_by_index(2)
driver.find_element_by_xpath("/html/body/div/div[4]/div[3]/div[1]/div[2]/button[2]").click()
time.sleep(15)
driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div/div/div[2]/button").click()
driver.find_element_by_xpath("/html/body/div/div[5]/div/div/button").click()
time.sleep(3)


####### evaluation#######
target = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]")
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()

target = driver.find_element_by_xpath("/html/body/div/div[4]")
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()

driver.find_element_by_xpath("/html/body/div/div[4]/div[3]/div[3]/div[2]/button[2]").click()
driver.find_element_by_xpath("/html/body/div/div[4]/div[4]/div/div[2]/div[3]/button").click()
'''