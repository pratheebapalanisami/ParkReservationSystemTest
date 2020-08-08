import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class AAF_Test10(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_customersearch(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://aafield.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/a/b').click()
        #time.sleep(0.5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("Naveen")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("maverick1a")
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/div/form/p[3]/input').click()
        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li/a')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/nav/div/div[1]/p/a[4]').click()
        add_park = driver.find_element_by_xpath(
            '//*[@id="Park"]').click()
        select_park_button_add_park = Select(driver.find_element_by_id('Park'))
        (select_park_button_add_park).select_by_visible_text('Elmwoood')
        time.sleep(0.5)
        add_county = driver.find_element_by_xpath(
            '//*[@id="Location"]').click()
        select_park_button_add_county = Select(driver.find_element_by_id('Location'))
        (select_park_button_add_county).select_by_visible_text('Douglas')
        time.sleep(0.5)

        startDate = driver.find_element_by_id('publishDateMin')
        startDate.send_keys('06/06/2020')
        time.sleep(3)

        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div/form/div[4]/button').click()
        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/p[3]/b')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()