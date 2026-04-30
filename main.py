import time
import data
import helpers
from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes.")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)



# 1.Definir o endereço:
    def test_set_route(self):
        assert self.driver.find_element(By.XPATH, "//div[contains(@class,'type-picker')]").is_displayed()


# 2.Selecionar o plano Comfort
    def test_select_plan(self):
        self.page.select_personal_mode()
        self.page.select_taxi_icon()
        self.page.click_call_taxi()

        comfort_route = self.driver.find_element(By.XPATH, "//div[contains(@class,'tcard')][.//img[@alt='Comfort']]"        )
        # verifica se não está ativo
        if "active" not in comfort_route.get_attribute("class"):
            comfort_route.click()
        # valida que está selecionado
        assert "active" in comfort_route.get_attribute("class")


# 3.Preencher o número de telefone
    def test_fill_phone_number(self):
        self.page.open_comfort_flow()
        self.page.fill_phone_flow(data.PHONE_NUMBER)

        code = helpers.retrieve_phone_code(self.driver)
        self.page.fill_code(code)
        self.page.confirm_code()


# 4.Adicionar um cartão de crédito
    def test_fill_card(self):
        self.page.open_comfort_flow()

        self.page.click_payment_method()
        self.page.click_add_card()

        self.page.fill_card_number_and_code(data.CARD_NUMBER,data.CARD_CODE)

        # clique fora para ativar o botão)
        self.page.click_outside()

        # Clica no botão "Adicionar"
        self.page.click_add_button()
        self.page.close_flow_card_button


# 5.Escrever um comentário para o motorista;
    def test_comment_for_driver(self):
        self.page.open_comfort_flow()
        self.page.add_comment(data.MESSAGE_FOR_DRIVER)


# 6.Pedir um cobertor e lenços
    def test_order_blanket_and_handkerchiefs(self):
        self.page.open_comfort_flow()
        self.page.toggle_blanket_and_tissues()


# 7.Pedir 2 sorvetes;
    def test_order_2_ice_creams(self):
        self.page.open_comfort_flow()
        self.page.add_ice_cream(2)
        time.sleep(3)

# 8.Pedir um táxi com a tarifa "Comfort".
    def test_car_search_model_appears(self):
        self.page.open_comfort_flow()
        self.page.fill_phone_flow_complete(data.PHONE_NUMBER)

        self.page.click_payment_method()
        self.page.click_add_card()

        self.page.fill_card_number_and_code(data.CARD_NUMBER, data.CARD_CODE)

        # clique fora para ativar o botão)
        self.page.click_outside()

        # Clica no botão "Adicionar"
        self.page.click_add_button()
        self.page.close_flow_card_button
        self.driver.implicitly_wait(5)
        self.page.add_comment(data.MESSAGE_FOR_DRIVER)
        self.wait_overlay_disappear()

        self.page.toggle_blanket_and_tissues()
        time.sleep(3)












    @classmethod
    def teardown_class(cls):
        cls.driver.quit()