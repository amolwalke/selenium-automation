from selenium import webdriver
import time
import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   #explicit

driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe"")

driver.get("https://www.saucedemo.com/")

driver.maximize_window()


time.sleep(5)

driver.implicitly_wait(10)   #command for wait every element in the code

driver.find_element_by_id("user-name").send_keys("standard_user")

driver.find_element_by_id("password").send_keys("secret_sauce")

#assert "standard_user" in driver.user-name



driver.find_element_by_id("login-button").click()

if validators.url("https://www.saucedemo.com/inventory.html"):  ##validating url link
    print("Login successfully")
else:
    print("invalid username or password")

driver.find_element_by_xpath("//select[@class='product_sort_container']/option[text()='Price (high to low)']").click()  #select[@class="product_sort_container"]


wait = WebDriverWait(driver,10)

ele = wait.until(EC.visibility_of(driver.find_element_by_class_name("inventory_item_name")))

time.sleep(7)
# //tag[@attributename='value']/subtag
driver.find_element_by_xpath("//a[@id='item_0_img_link']/img[@class='inventory_item_img']").click()

time.sleep(4)
d= driver.find_element_by_xpath("//button[text()='ADD TO CART']")
print(d.is_displayed())
d.click()


v = driver.find_element_by_xpath("//div[@id='shopping_cart_container']/a[@class='shopping_cart_link fa-layers fa-fw']")
print(v.is_selected())
v.click()
time.sleep(7)

q=driver.find_element_by_xpath("//div[@class='cart_footer']/a[@class='btn_action checkout_button']")
print(q.is_displayed())
q.click()
time.sleep(4)

driver.find_element_by_id("first-name").send_keys("Amol")
driver.find_element_by_id("last-name").send_keys("walke")
driver.find_element_by_id("postal-code").send_keys("400012")

driver.find_element_by_xpath("//div[@class='checkout_buttons']/input[@class='btn_primary cart_button']").click()
driver.find_element_by_xpath("//div[@class='cart_footer']/a[@class='btn_action cart_button']").click()









