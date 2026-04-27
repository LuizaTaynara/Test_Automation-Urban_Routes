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

    def test_set_route(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.get_from_locator() == data.ADDRESS_FROM
        assert self.page.get_to_locator() == data.ADDRESS_TO
        time.sleep(10)

    def test_select_plan(self):
        # Adicionar em S8
        print("função criada para definir o mapa")
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("função criada para definir o numero de telefone")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("função criada para definir o cartão para pagamento")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("função criada para adicionar um comentário ao motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("função criada para adicionar coberto e lenços")
        pass



    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("função criada para mostrar o modelo do carro encontrado")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()