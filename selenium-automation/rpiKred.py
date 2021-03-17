from selenium import webdriver
import time

driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

#driver.get("https://app.kredily.com/login/?_ga=2.140671026.1237576302.1614748823-445720262.1614748823")
driver.maximize_window()
driver.implicitly_wait(10)



#login 
user = ['amolw@kaninnovations.com','vineetk@kaninnovations.com']
password = ['Amol1400','Tellmehow123!@#']
for n in range(len(user)):
    driver.get("https://app.kredily.com/login/?_ga=2.140671026.1237576302.1614748823-445720262.1614748823")
    a = driver.find_element_by_id("signInFormEmailAddress")
    a.send_keys(user[n])
    b = driver.find_element_by_id("signInFormPassword")
    b.send_keys(password[n])

    driver.find_element_by_class_name("custom-checkbox-label").click()

    driver.find_element_by_id("signinSubmitBtn").click()
    
    time.sleep(7)
    '''
    driver.find_element_by_id("clockInBtn").click()

    
    driver.find_element_by_class_name("action-menu-list for_mobile_view_action_menu_list")
    driver.find_element_by_xpath("//ul/a[text()='Log Out']").click()
    '''
    driver.get("https://app.kredily.com/accounts/logout")