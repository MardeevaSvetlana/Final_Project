
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base


class Clear_cart_page(Base):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver= driver

    # Locators

    cart_button= "//*[@id='js-cart-wrapper']/span[1]"
    delete_button= "//span[@title='Удалить из корзины']"
    amount_cart = "//span[@class ='s-count js-cart-count']"


    # Gettens


    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))


    def get_delete_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_button)))


    def get_amount_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.amount_cart)))

        # Actions

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    def click_delete_button(self):
        self.get_delete_button().click()
        print("Click delete button")


    # Methods

    def clear(self):
        self.driver.back()
        self.driver.back()
        self.driver.back()
        self.driver.back()
        self.assert_url("https://russkaja-ohota.ru/cart/")
        self.click_delete_button()
        self.driver.back()
        self.driver.back()
        self.get_current_url()
        self.driver.execute_script("window.scrollTo(0,500)")
        self.assert_word(self.get_amount_cart(), '0')





















