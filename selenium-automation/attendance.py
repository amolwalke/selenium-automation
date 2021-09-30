from selenium import webdriver
import time

driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("https://app.kredily.com/login/?_ga=2.140671026.1237576302.1614748823-445720262.1614748823")
driver.maximize_window()
driver.implicitly_wait(10)

a = driver.find_element_by_id("signInFormEmailAddress")
a.send_keys("amolw@kaninnovations.com")   ##8459156668
b = driver.find_element_by_id("signInFormPassword")
b.send_keys("Amol1400")   ##Float(1)

driver.find_element_by_class_name("custom-checkbox-label").click()

driver.find_element_by_id("signinSubmitBtn").click()
 
time.sleep(7)

#driver.find_element_by_id("clockInBtn").click()

##attendance
driver.find_element_by_id("tourdemo3").click()




try:
    ex = driver.find_element_by_id("adminToggleContainerLI")
    ex.click()


except:
    print("not found")


driver.find_element_by_id("month_log_tab").click()
try:

    rData = []
    row = driver.find_elements_by_xpath("/html/body/div[7]/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[2]/div/table/tbody/tr[1]")
    print(row)                             
    for webElement in row:
        rData.append(webElement.text)

    #length = driver.find_elements_by_xpath("//tr[@role='row']/td[@class='sorting_1']")

    print(rData[0])


    pData = []
    row1 = driver.find_elements_by_xpath("//tbody/tr[1]/td[9]")
    print(row1)                             
    for webElement in row1:
        pData.append(webElement.text)
   
    print(pData[0])
    
except:pass
#length = driver.find_elements_by_xpath("//tr[@role='row']/td[@class='sorting_1']")

##if pData[0] == 'Leave':


    
#if pData[0] == '':

    


    




