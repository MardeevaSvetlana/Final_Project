import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base


class Client_Information_page(Base):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver= driver

    # Locators

    last_name = "//*[@title='Фамилия']"
    first_name = "//*[@title='Имя']"
    telephon_number= "//*[@title='Телефон']"
    email= "//*[@title='Email']"
    town= "//*[@title='Город, поселок']"
    agreement_button= "//*[@id='s-contact-form']/div/div[1]/div[1]/div[7]/div/label/input[2]"
    continue_button= "//*[@id='step-contactinfo']/footer/input[1]"
    radio_button= "//*[@id='step-shipping']/div/div/ul/li[1]/div[1]/div[1]/h3/label/input"
    town_final= "//*[@title='Город, поселок']"
    address= "//*[@title='Улица, дом, квартира']"
    index= "//*[@title='Индекс']"
    continue_btn= "//*[@id='step-shipping']/footer/input[1]"

    # Gettens

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_telephon_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephon_number)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_town(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.town)))

    def get_agreement_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.agreement_button)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_radio_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radio_button)))


    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_town_final(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.town_final)))

    def get_index(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.index)))


    def get_continue_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))


    # Actions # шаги

    def input_last_name(self, last_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(last_name)
        print("input last name")

    def input_first_name(self, first_name):
        self.get_first_name().clear()
        self.get_first_name().send_keys(first_name)
        print("input first name")
        
    def input_telephon_number(self, number):
        self.get_telephon_number().clear()
        self.get_telephon_number().send_keys(number)
        print("input telephon number")

    def input_email(self, email):
        self.get_email().clear()
        self.get_email().send_keys(email)
        print("input email")

    def input_town(self, town):
        self.get_town().clear()
        self.get_town().send_keys(town)
        print("input town")


    def click_agreement_button(self):
        self.get_agreement_button().click()
        self.get_agreement_button().click()
        print("Click agreement button")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")

    def click_radio_button(self):
        self.get_radio_button().click()
        print("Click radio button")

    def input_town_final(self, town_final):
        self.get_town_final().clear()
        self.get_town_final().send_keys(town_final)
        print("input town final")

    def input_address(self, address):
        self.get_address().clear()
        self.get_address().send_keys(address)
        print("input address")

    def input_index(self, index):
        self.get_index().clear()
        self.get_index().send_keys(index)
        print("input index")

    def click_continue_btn(self):
        self.get_continue_btn().click()
        print("Click continue button")


    # Methods

    def input_information(self):
        self.get_current_url()
        self.input_last_name("Ivanov")
        self.input_first_name("Ivan")
        self.input_telephon_number("89232472689")
        self.input_email("svir8080@mail.ru")
        self.input_town('Новосибирск')
        self.click_agreement_button()
        self.click_continue_button()
        self.assert_url('https://russkaja-ohota.ru/checkout/shipping/')
        self.click_radio_button()
        self.input_town_final('Новосибирск')
        self.input_address('Гоголя')
        self.input_index('123456')
        self.driver.execute_script("window.scrollTo(0,1000)")
        self.click_continue_btn()
        self.assert_url('https://russkaja-ohota.ru/checkout/payment/')







