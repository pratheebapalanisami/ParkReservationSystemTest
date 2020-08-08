import unittest
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AAF_Test16(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_viewbooking(self):

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
        view_bookings= driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/button[4]/a').click()
        time.sleep(3.0)
        try:
            Booking_page = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div/div[1]/h2')
            assert True
        except NoSuchElementException:
            self.fail("Failed to View bookings")
            assert False



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
