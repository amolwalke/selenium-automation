from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   #explicit
from selenium.webdriver.common.action_chains import ActionChains #scrolling pages


driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

#driver.execute_script("window.scrollBy(0,600)","")
time.sleep(5)


xp=["box7","box6","box5","box4","box3","box2","box1"]

xn =["box107","box106","box105","box104","box103","box102","box101"]


zip_object = zip(xp, xn)
for element1, element2 in zip_object:
    source= driver.find_element_by_id(element1)
    
    target = driver.find_element_by_id(element2)
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target)
    actions.perform()
   


# for r in xp:
#     for q in qw:    
    
#         if count == n+1:
#             break 
    
#         source= driver.find_element_by_id(r)
    
#         target = driver.find_element_by_id(q)
#         actions = ActionChains(driver)
#         actions.drag_and_drop(source, target)
#         actions.perform()

