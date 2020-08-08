import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AAF_Test3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_forgotpassword(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://aafield.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/a/b').click()
        #time.sleep(0.5)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/div/p/a').click()
        #time.sleep(0.5)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("groyce@unomaha.edu")
        #time.sleep(0.5)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/form/p[2]/input').click()
        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/p[1]')
            assert True
        except NoSuchElementException:
            self.fail("Password Reset Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()