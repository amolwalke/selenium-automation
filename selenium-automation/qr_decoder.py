from pyzbar.pyzbar import decode
from PIL import Image
from selenium import webdriver

driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

img = Image.open('C:\\Users\\Amol\\Documents\\Example-QR-code.jpg')
result = decode(img)

for i in result:
    a = print(i.data.decode("utf-8"))
    b=str(a)
    driver.get(b)
    



    

    
