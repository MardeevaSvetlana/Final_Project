
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base


class Login_page(Base):

    url= 'https://russkaja-ohota.ru/'

    def __init__(self,driver):
        super().__init__(driver)
        self.driver= driver

    # Locators
    start_button="//a[@class='s-link']"
    user_name = "//input[@placeholder='Email']"
    passwort = "//input[@name='password']"
    login_button= "//input[@class='wa-login-submit']"


    # Gettens

    def get_start_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.start_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.passwort)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # Actions

    def click_start_button(self): # описываем, что делать с данной кнопкой
        self.get_start_button().click()
        print("Click start button")

    def input_user_name(self, user_name): # описываем, что делать с данной кнопкой
        self.get_user_name().send_keys(user_name)
        print("input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input passwort")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")


    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_start_button()
        self.input_user_name("svir8080@mail.ru")
        self.input_password("123456")
        self.click_login_button()
        self.assert_url('https://russkaja-ohota.ru/my/orders/')




