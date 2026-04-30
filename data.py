import time
import data
import helpers
from selenium import webdriver
from selenium.webdriver import chrome
from helpers import retrieve_phone_code


URBAN_ROUTES_URL = 'https://cnt-26652a4b-7351-4c90-9639-997213206bd0.containerhub.tripleten-services.com?lng=pt'
ADDRESS_FROM = 'East 2nd Street, 601'
ADDRESS_TO = '1300 1st St'
PHONE_NUMBER = '+1 123 123 12 12'
CARD_NUMBER = '1234 5678 9100'
CARD_CODE = '1111'
MESSAGE_FOR_DRIVER = 'Pare no bar de sucos'

