
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver= driver

    # Locators
    main_word= "//*[@id='js-main-block']/h1"
    checkout_button = "//*[@id='s-cart-page']/form/div[2]/section/div/table/tbody/tr[3]/td/input"



    # Gettens

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions


    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")


    # Methods

    def product_confirmation(self):
        self.get_current_url()
        self.click_checkout_button()
        self.assert_url('https://russkaja-ohota.ru/checkout/')







