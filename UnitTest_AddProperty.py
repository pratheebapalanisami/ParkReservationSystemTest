import unittest
import unittest
import time
#import org.openqa.selenium.support.ui.Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class AAF_Test13(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addproperty(self):

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
        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li/a')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            #assert Falsetime.sleep(3.0)
        select_park= driver.find_element_by_xpath('// *[ @ id = "app-layout"] / div / div / div / div / div / div[5] / div / h4 / a').click()
        time.sleep(3.0)
        add_property_button = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/p[10]/a[3]').click()
        time.sleep(3.0)
        select_park_button_add_property = Select(driver.find_element_by_xpath('//*[@id="id_Park_Name"]'))
        (select_park_button_add_property).select_by_visible_text('Elmwoood')
        #dropdown.selectByValue('Elmwood park')
        property_name = driver.find_element_by_id('id_Property_Name').send_keys("Squash court")
        description = driver.find_element_by_id('id_Property_Description').send_keys("Clean and well maintained")
        guest_capacity = driver.find_element_by_id('id_Property_Guest_Capacity').send_keys("20")
        price = driver.find_element_by_id('id_Price').send_keys("$80.00")
        time.sleep(3.0)
        add_property_button = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div[2]/form/div[8]/button').click()

        try:
            added_property = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/button[1]/a/b')
            assert True
        except NoSuchElementException:
            self.fail("Failed to add property")
            assert False



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
