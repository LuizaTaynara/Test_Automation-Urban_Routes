import time
import data
import helpers
from selenium import webdriver
from selenium.webdriver import chrome
from helpers import retrieve_phone_code
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    from_locator = (By.ID, 'from')   # From
    to_locator = (By.ID, 'to')       # To

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def _find(self, locator):
        return self.driver.find_element(*locator)

    def _click(self, locator):
        self.driver.find_element(*locator).click()

    def _type(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator):
        element = self.driver.find_element(*locator).text
        return element

    def _get_value(self, locator):
        return self._find(locator).get_attribute('value')

    def enter_locations(self, from_text, to_text):
        self._type(self.from_locator, from_text)
        self._type(self.to_locator, to_text)

    def get_from_locator(self):
        return self._get_value(self.from_locator)

    def get_to_locator(self):
        return self._get_value(self.to_locator)



def test_order_2_ice_creams(self):
    order_ice_cream = 2
    for count in range(order_ice_cream):
        # Adicionar em S8
        print("função criada para pedir sorvete")
    pass