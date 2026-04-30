import time
import data
import helpers
from selenium import webdriver
from helpers import retrieve_phone_code
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # Locators
    from_locator = (By.ID, 'from')  # From
    to_locator = (By.ID, 'to')  # To

    open_route = (By.XPATH, "//div[contains(@class,'type-picker')]")

    personal_option_locator = (By.XPATH, '//div[text()="Personal"]')
    icon_taxi_locator = (By.XPATH, "//img[contains(@src, 'taxi')]")
    call_taxi_button = (By.XPATH, "//button[@class='button round' and contains(text(),'Chamar um táxi')]")
    comfort_mode = (By.XPATH, "//img[contains(@src, 'kids')]")

    number_locator = (By.XPATH, "//div[text()='Número de telefone']")
    phone_input = (By.ID,'phone')
    code_phone_input = (By.ID,'code')
    submit_phone = (By.XPATH, "//button[@type='submit' and text()='Próximo']")
    confirm_phone_button = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")

    payment_button = (By.XPATH, "//div[contains(text(),'Método de pagamento')]")
    add_card_button = (By.XPATH, "//div[contains(@class,'pp-plus-container')]")
    card_number = (By.XPATH, "//input[@placeholder='1234 0000 4321']")
    card_code = (By.XPATH, "//input[@placeholder='12']")
    add_button = (By.XPATH, "//button[text()='Adicionar']")
    outside_area = (By.CSS_SELECTOR, "body")
    close_flow_card_button = (By.XPATH, "//button[contains(@class,'section-close')]")


    comment_input = (By.ID, "comment")

    blanket_toggle = (By.XPATH, "//span[contains(@class,'slider')]/..")

    order_ice_cream = (By.XPATH, "//div[@class='counter-plus']")

# essencials actions

    def _find(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def _click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def _type(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def _wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))





#1


    def enter_from_location(self, from_text):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.from_locator))
        self.driver.find_element(*self.from_locator).send_keys(from_text)

    def enter_to_location(self, to_text):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.to_locator))
        self.driver.find_element(*self.to_locator).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_from_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.from_locator)
        ).get_attribute('value')

    def get_to_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.to_locator)
        ).get_attribute('value')

    def get_from_locator(self):
        return self.get_value(self.from_locator)

    def get_to_locator(self):
        return self.get_value(self.to_locator)

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
        element = self.wait.until(EC.presence_of_element_located(self.comfort_mode))
        classes = element.get_attribute("class") or ""
        return "active" in classes

    def select_comfort(self):
        element = self._wait(self.comfort_mode)



#3

    def fill_phone_flow(self, phone):
        self._click(self.number_locator)
        self._type(self.phone_input, phone)
        self._click(self.submit_phone)


    def fill_code(self, code):
        self._type(self.code_phone_input, code)

    def confirm_code(self):
        self._click(self.confirm_phone_button)

#4
    def click_payment_method(self):
        element=WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.payment_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_add_card(self):
        self._click(self.add_card_button)

    def fill_card_number_and_code(self, number, code):
        self._type(self.card_number, number)
        self._type(self.card_code, code)

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_button)
        ).click()

    def close_flow_card(self):
        try:
            self._click(self.close_flow_card_button)
        except:
            pass

#5

    def add_comment(self, text):
        self._type(self.comment_input, text)

#6
    def toggle_blanket_and_tissues(self):
        self._click(self.blanket_toggle)


#7
    def add_ice_cream(self, quantity):
        for count in range(quantity):
            self._click(self.order_ice_cream)

#8
    def open_comfort_flow(self):
        self._click(self.personal_option_locator)
        self._click(self.icon_taxi_locator)
        self._click(self.call_taxi_button)
        self._click(self.comfort_mode)


    def complete_phone_flow(self, phone):
        self._click(self.phone_input)
        self._type(self.phone_input, phone)
        self._click(self.submit_phone)

        code = helpers.retrieve_phone_code(self.driver)
        self._type(self.code_phone_input, code)
        self._click(self.confirm_phone_button)


    def complete_payment_flow(self, number, code):
        self._click(self.payment_button)
        self._click(self.add_card_button)

        self._type(self.card_number, number)
        self._type(self.card_code, code)

        self.click_outside()
        self.driver.find_element(*self.add_button).click()
        self.click(self.close_flow_card_button)
        time.sleep(3)


    def complete_order_flow(self, phone, card_number, card_code, comment):
        self.complete_phone_flow(phone)
        self.add_comment(comment)
        self.add_ice_creams(2)
        self.toggle_blanket()
        self.complete_payment_flow(card_number, card_code)
        time.sleep(3)














