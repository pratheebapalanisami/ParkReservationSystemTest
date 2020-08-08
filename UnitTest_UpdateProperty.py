import unittest
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
#import org.openqa.selenium.JavascriptExecutor;


class AAF_Test15(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_updateproperty(self):

        driver = self.driver
        #JavascriptExecutor je = (JavascriptExecutor) driver;
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
        select_park= driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div[1]/div/a/img').click()
        time.sleep(0.5)
        select_property = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div[2]/a[2]').click()
        update_property = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/p[5]/a[1]').click()
        time.sleep(0.5)
        property_name = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div[2]/form/div[2]/div/div/div/input').send_keys("test")
        time.sleep(0.5)
        update_property_button = driver.find_element_by_name('viewslot')
        webdriver.ActionChains(driver).move_to_element(update_property_button).click(update_property_button).perform()
        time.sleep(0.5)
        try:
            updated_property = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/button[1]/a/b')
            assert True
        except NoSuchElementException:
            self.fail("Failed to edit property")
            assert False



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
