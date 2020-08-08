import unittest
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class AAF_Test17(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_assignmaintanence(self):

        driver = self.driver
        driver.maximize_window()
        driver.get(" https://aafield.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/a/b').click()
        time.sleep(0.5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("Pratheeba")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("maverick1a")
        login = driver.find_element_by_xpath(
            '//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/div/form/p[3]/input').click()
        assign_maintanance = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/button[2]/a/b').click()
        time.sleep(3.0)
        assign_maintanance_link = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div/div[2]/table/tbody/tr/td[6]/a').click()
        select_maintanance_person = Select(driver.find_element_by_id('Location'))
        (select_maintanance_person).select_by_visible_text('Preethi')
        assign_maintanance_button = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/form/div[5]/button').click()
        try:
            assigned = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/button[1]/a/b')
            assert True
        except NoSuchElementException:
            self.fail("Failed to assign")
            assert False



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
