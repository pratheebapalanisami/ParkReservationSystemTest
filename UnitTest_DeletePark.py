import unittest
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AAF_Test20(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_deletepark(self):

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
        select_park = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div[5]/div/a/img').click()
        time.sleep(3.0)
        delete_park = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/p[11]/a[2]').click()
        try:
            deleted = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/button[1]/a/b')
            assert True
        except NoSuchElementException:
            self.fail("Failed to delete park")
            assert False



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
