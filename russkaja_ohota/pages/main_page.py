import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

        def __init__(self, driver):
            super().__init__(driver)
            self.driver = driver

        # Locators
        exp_directory = "//a[@title='Развернутый каталог']"
        directory= "//div[@class='s-catalog-wrapper is-big']"
        section_button= "// a[@ href ='/category/radiostancii-eholoty-barometry-navigatory-kompasy/']"
        search_line= "//*[@id='s-header-wrapper']/div[1]/div/div[2]/div/div[1]/div/form/input[1]"
        search_button= "//*[@class='s-submit-input']"
        buy_button= "//*[@id='js-content-block']/div/section/ul/li[7]/div/div[4]/form/div/div/div[1]/input"
        cart_button= "//*[@id='js-cart-wrapper']/a"
        value_product= "//*[@id='js-content-block']/div/section/ul/li[7]/div/div[2]/h5/a/text()"
        value_price_product= "//*[@id='js-content-block']/div/section/ul/li[7]/div/div[3]"

        # Gettens
        def get_exp_directory(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exp_directory)))

        def get_directory(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.directory)))

        def get_section_button(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.section_button)))

        def get_search_line(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_line)))

        def get_search_button(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

        def get_buy_button(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

        def get_cart_button(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))


        # Actions
        def click_exp_directory(self):
            self.get_exp_directory().click()
            print("Click expanded directory")

        def click_directory(self):
            self.get_directory().click()
            print("Click directory")

        def click_section_button(self):
            self.get_section_button().click()
            print("Click section button")

        def input_search_line(self,product_name):
            self.get_search_line().send_keys(product_name)
            print("Input product name")

        def click_search_button(self):
            self.get_search_button().click()
            print("Click search button")

        def click_buy_button(self):
            self.get_buy_button().click()
            print("Click buy button")

        def click_cart_button(self):
            self.get_cart_button().click()
            print("Click cart button")

        # Methods
        def select_product(self):
            with allure.step("Select product"):
                Logger.add_start_step(method="select_product")
                self.get_current_url()
                self.click_exp_directory()
                self.click_directory()
                self.click_section_button()
                self.assert_url('https://russkaja-ohota.ru/category/radiostancii-eholoty-barometry-navigatory-kompasy/')
                self.input_search_line("Ноутбук")
                self.click_search_button()
                self.driver.execute_script("window.scrollTo(0,1000)")
                self.get_screenshot()
                self.click_buy_button()
                self.click_cart_button()
                Logger.add_end_step(url=self.driver.current_url, method="select_product")



















