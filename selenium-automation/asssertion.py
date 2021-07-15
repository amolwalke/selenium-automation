
import unittest
from selenium import webdriver
  
class Test(unittest.TestCase):
    # test function to test equality of two value
    def test_negative(self):
        driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")
        driver.get("https://www.google.com/")
        title =driver.title
        # assertEqual() to check equality of first & second value
        self.assertEqual("Google",title,"non correct")
  
if __name__ == '__main__':
    unittest.main()
