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




URBAN_ROUTES_URL = 'https://cnt-301919a0-2646-478d-8010-4159c31387c0.containerhub.tripleten-services.com?lng=pt'
ADDRESS_FROM = 'East 2nd Street, 601'
ADDRESS_TO = '1300 1st St'
PHONE_NUMBER = '+1 123 123 12 12'
CARD_NUMBER = '1234 5678 9100'
CARD_CODE = '1111'
MESSAGE_FOR_DRIVER = 'Pare no bar de sucos'

PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
CAMPING_LOCATOR = (By.XPATH, '//div[contains(text(),"Camping")]')
AUDI_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Audi A3 Sedã")]')
ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, '(//div[contains(text(),"Adicionar carteira de motorista")])[2]')
FIRST_NAME_LOCATOR = (By.ID, 'firstName')
LAST_NAME_LOCATOR = (By.ID, 'lastName')
DATE_OF_BIRTH_LOCATOR = (By.ID, 'birthDate')
NUMBER_LOCATOR = (By.ID, 'number')
ADD_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and text()="Add"]')
ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Add a driver")]')
VERIFICATION_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Thank you")]')
DURATION_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Duração")]')