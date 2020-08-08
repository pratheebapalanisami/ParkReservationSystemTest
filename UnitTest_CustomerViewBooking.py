import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AAF_Test11(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_viewbooking(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://aafield.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/a/b').click()
        #time.sleep(0.5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("Naveen")
        elem = driver.find_element_by_id("id_password")
        #time.sleep(1)
        elem.send_keys("maverick1a")
        #time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/div/form/p[3]/input').click()
        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/button/a/b')
            assert True
        except NoSuchElementException:
            self.fail("Maintanence Login Failed")
            assert False

        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/button/a/b').click()

        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div/div[2]/table/thead/tr/th[1]')
            assert True
        except NoSuchElementException:
            self.fail("View Booking failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()