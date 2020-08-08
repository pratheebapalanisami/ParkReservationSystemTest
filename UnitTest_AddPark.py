import unittest
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AAF_Test12(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addpark(self):

        driver = self.driver
        driver.maximize_window()
        driver.get(" https://aafield.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/a/b').click()
        time.sleep(0.5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("Pratheeba")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("maverick1a")
        elem = driver.find_element_by_xpath(
            '//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/div/form/p[3]/input').click()

        add_park_button = driver.find_element_by_class_name('btn-outline-primary').click()
        time.sleep(3.0)
        park_name = driver.find_element_by_id('id_Park_Name').send_keys("Elmwoood")
        park_address = driver.find_element_by_id('id_Park_Address').send_keys("Pacific street")
        park_county = driver.find_element_by_id('id_County').send_keys("Douglas")

        time.sleep(3.0)
        submit_button = driver.find_element_by_xpath(
            '/html/body/div/div/div/div/div/div/div/div[2]/form/div[5]/button').click()
        time.sleep(3.0)
        try:
            added_park = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/button[1]/a/b')
            assert True
        except NoSuchElementException:
            self.fail("Failed to add park")
            assert False



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
