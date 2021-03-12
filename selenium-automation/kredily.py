from selenium import webdriver
import time

driver = webdriver.Chrome(r"D:\New folder (2)\chromedriver.exe")

driver.get("https://app.kredily.com/login/?_ga=2.140671026.1237576302.1614748823-445720262.1614748823")
driver.maximize_window()
driver.implicitly_wait(10)

a = driver.find_element_by_id("signInFormEmailAddress")
a.send_keys("9167087078")
b = driver.find_element_by_id("signInFormPassword")
b.send_keys("Amranaaz@1995")

#driver.find_element_by_class_name("custom-checkbox-label").click()

driver.find_element_by_id("signinSubmitBtn").click()
 
time.sleep(7)
driver.find_element_by_id("clockInBtn").click()

'''
c= driver.find_element_by_id("tourdemo4")
c.click()

time.sleep(7)
p=driver.find_element_by_xpath("//div[@class='title pb-1']/button[@class='btn btn-primary float-right btn-small-primary waves-effect waves-light']")
p.click()


p = driver.find_element_by_xpath("//fieldset[@class='form-group']/input[@id='leaveStartDatePicker']").send_keys("26-3-2021")
driver.find_element_by_xpath("//fieldset[@class='form-group']/input[@id='leaveEndDatePicker']").send_keys("27-3-2021")

driver.find_element_by_id("leaveReasonInput").send_keys("Travelling to native place.")
driver.find_element_by_id("regularLeaveSubmit").click()

#w = driver.find_element_by_xpath("//")


#driver.find_element_by_xpath("//div[@id='addToCart_feature_div']/div[@class='a-button-stack']/span[@class='a-declarative']/span[@id='submit.add-to-cart']").click()
'''