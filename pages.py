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
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # Locators
    from_locator = (By.ID, 'from')  # From
    to_locator = (By.ID, 'to')  # To

    personal_option_locator = (By.XPATH, '//div[text()="Personal"]')
    icon_taxi_locator = (By.XPATH, "//img[contains(@src, 'taxi')]")
    call_taxi_button = (By.XPATH, "//button[@class='button round' and contains(text(),'Chamar um táxi')]")
    comfort_mode = (By.XPATH, "//img[contains(@src, 'kids')]")

    number_locator = (By.XPATH, "//div[text()='Número de telefone']")
    phone_input = (By.ID,'phone')
    phone_code_input = (By.ID,'code')
    submit_phone = (By.XPATH, "//button[@type='submit' and text()='Próximo']")
    confirm_phone_button = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")

    payment_method_button = (
        By.XPATH,
        "//div[text()='Método de pagamento']/ancestor::div[contains(@class,'pp-button')]"
    )
    add_card_button = (By.XPATH, "//div[contains(@class,'pp-plus-container')]")
    card_number_input = (By.XPATH, "//input[@placeholder='1234 0000 4321']")
    card_code_input = (By.XPATH, "//input[@placeholder='12']")
    add_button = (By.XPATH, "//button[text()='Adicionar']")
    outside_area = (By.CSS_SELECTOR, "body")
    close_flow_card_button = (By.XPATH, "//button[@class='close-button section-close']")

    comment_input = (By.ID, "comment")

    blanket_toggle = (By.XPATH, "//span[contains(@class,'slider')]/..")
    blanket_switch = (By.XPATH, "//span[contains(@class,'slider')]")

    order_ice_cream = (By.XPATH, "//div[@class='counter-plus']")

# Ações
    def _find(self, locator):
        return self.driver.find_element(*locator)

    def _click(self, locator):
        self.driver.find_element(*locator).click()

    def _type(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def _wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_outside(self):
        self._click(self.outside_area)

    def open_comfort_flow(self):
        self.select_personal_mode()
        self.select_taxi_icon()
        self.click_call_taxi()
        self.select_comfort_method()

#1

    def enter_locations(self, from_text, to_text):
        self._type(self.from_locator, from_text)
        self._type(self.to_locator, to_text)

    def get_from_locator(self):
        return self._get_value(self.from_locator)

    def get_to_locator(self):
        return self._get_value(self.to_locator)

#2

    def select_personal_mode(self):
        self.driver.find_element(*self.personal_option_locator).click()

    def select_taxi_icon(self):
        self.driver.find_element(*self.icon_taxi_locator).click()

    def click_call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def select_comfort_method(self):
        self.wait.until(EC.element_to_be_clickable(self.comfort_mode)).click()

    def is_comfort_selected(self):
        element = self.driver.find_element(*self.comfort_mode)
        return element.get_attribute("alt") == "Comfort"

    def is_comfort_active(self):
        element = self.wait.until(EC.presence_of_element_located(self.comfort_card))
        classes = element.get_attribute("class") or ""
        return "active" in classes

    def select_comfort(self):
        element = self._wait(self.COMFORT)

        # evita clique desnecessário
        if "active" not in element.get_attribute("class"):
            element.click()

#3

    def fill_phone_flow(self, phone):
        self._click(self.number_locator)
        self._type(self.phone_input, phone)
        self._click(self.submit_phone)


    def fill_code(self, code):
        self._type(self.phone_code_input, code)

    def confirm_code(self):
        self._click(self.confirm_phone_button)

#4
    def click_payment_method(self):
        element=WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.payment_method_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_add_card(self):
        self._click(self.add_card_button)

    def fill_card_number_and_code(self, number, code):
        self._type(self.card_number_input, number)
        self._type(self.card_code_input, code)

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_button)
        ).click()

    def close_flow_card(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_flow_card_button)
        ).click()

#5

    def add_comment(self, text):
        self._type(self.comment_input, text)

#6
    def toggle_blanket_and_tissues(self):
        self._click(self.blanket_toggle)

    def is_blanket_enabled(self):
        element = self.driver.find_element(*self.blanket_switch)
        return "checked" in element.get_attribute("class") or "active" in element.get_attribute("class")


#7
    def add_ice_cream(self, quantity):
        for count in range(quantity):
            element = self.driver.find_element(*self.order_ice_cream)
            element.click()

#8

    def fill_phone_flow_complete(self, phone):
        self.fill_phone_flow(phone)
        code = helpers.retrieve_phone_code(self.driver)
        self.fill_code(code)
        self.confirm_code()

    def fill_payment_flow_complete(self, number, code):
        self._click(self.payment_method_button)
        self._click(self.add_card_button)

        self._type(self.card_number_input, number)
        self._type(self.card_code_input, code)

        self._click(self.plc)

        self._click(self.add_button)
        self._click(self.close_flow_card_button)








