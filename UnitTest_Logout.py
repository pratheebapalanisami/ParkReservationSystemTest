import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AAF_Test2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_logout(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://aafield.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/a/b').click()

        elem = driver.find_element_by_id("id_username")
        elem.send_keys("instructor")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("instructor1a")
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/div/form/p[3]/input').click()


        try:
            # attempt to find the plus button - if found, logged in

            elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li/a')
            logout = True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

        if logout:
            elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li[2]/a').click()

            try:
               # find the 'edit' pencil icon - if post added, edit pate is displayed
               elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/div/p/a')
               assert True

            except NoSuchElementException:
                self.fail("Logout not successfull")
                assert False


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()

