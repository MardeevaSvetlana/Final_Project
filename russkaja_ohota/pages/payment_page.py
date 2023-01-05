import time

import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Payment_page(Base):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver= driver

    # Locators
    radio_btn= "//*[@id='step-payment']/div/div/ul/li[2]/h3/label/input"
    finish_button= "//*[@class='s-step-submit']"
    user_word= "//*[@class ='s-user-name']"


    # Gettens
    def get_radio_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radio_btn)))

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    def get_user_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_word)))





    # Actions
    def click_radio_btn(self):
        self.get_radio_btn().click()
        print("Click radio button")

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")


    # Methods

    def payment(self):
        with allure.step("Payment"):
            Logger.add_start_step(method="payment")
            self.get_current_url()
            self.click_radio_btn()
            self.click_finish_button()
            self.assert_url('https://russkaja-ohota.ru/checkout/confirmation/')
            self.assert_word(self.get_user_word(), 'Ivanov Ivan')
            Logger.add_end_step(url=self.driver.current_url, method="payment")





















