import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AAF_Test5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_signup(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://aafield.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/a/b').click()
        #time.sleep(0.5)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[3]/a[3]').click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("Employee97780")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("srividyagopaluni@gmail.com")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("16521 Hanover street")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_id("id_state")
        elem.send_keys("Nebraska")
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("68007")
        #time.sleep(1)
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("4028006133")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("maverick")
        #time.sleep(1)
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys("maverick")
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/form/div/button').click()
        #time.sleep(1)
        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/h1')
            assert True
        except NoSuchElementException:
            self.fail("Maintanence Registeration Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()