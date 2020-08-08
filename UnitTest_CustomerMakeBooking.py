import unittest
import time
from telnetlib import EC

from requests import session
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class AAF_Test9(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_booking(self):

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
        #elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div[5]/div/h4/a/b').click()
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div[2]/div/a/img').click()
        elem= driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/a[2]').click()
        startDate = driver.find_element_by_id('txtDate')
        startDate.send_keys('10/09/2020')

        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/form/div[2]/button').click()
        time.sleep(0.5)
        elem = driver.find_element_by_xpath('//*[@id="myForm"]/div[5]/div/input[2]').click()
        time.sleep(0.5)
        elem = driver.find_element_by_xpath('//*[@id="myForm"]/div[7]/button').click()
        time.sleep(0.5)



        #WebDriverWait(session, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "credit-card-number")))
        #WebDriverWait(session, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.number#credit-card-number"))).send_keys("0000000000000000")

        #edate = driver.find_element_by_id('braintree-hosted-field-expirationDate')
        #edate.send_keys('09/20')
        #ccnumber = driver.find_element_by_id('credit-card-number')
        #ccnumber.send_keys('4111111111111111')
        #edate = driver.find_element_by_id('braintree-hosted-field-expirationDate')
        #edate.send_keys('09/20')
        #cvv = driver.find_element_by_id('braintree-hosted-field-cvv')
        #cvv.send_keys('400')
        #postalcode  = driver.find_element_by_id('expiration')
        #postalcode.send_keys('40000')


        elem =  driver.find_element_by_xpath('//*[@id="payid"]').click
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/button/a/b').click()


        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li[2]/a')
            assert True
        except NoSuchElementException:
            self.fail("Booking Failed")
            assert False


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
