
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.clear_cart_page import Clear_cart_page
from pages.client_information_page import Client_Information_page

from pages.login_page import Login_page
from selenium.webdriver.chrome.options import  Options # для очистки консоли

from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_01_buy_product(set_up):
    options=Options() # для очистки консоли
    options.add_experimental_option('excludeSwitches', ['enable-loging']) # для очистки консоли
    driver = webdriver.Chrome(executable_path='C:\\Users\\sa.mardeeva\\PycharmProjects\\resource\\chromedriver.exe',chrome_options=options)


    lp= Login_page(driver)
    lp.authorization()

    mp=Main_page(driver)
    mp.select_product()

    cp= Cart_page(driver)
    cp.product_confirmation()

    ci= Client_Information_page(driver)
    ci.input_information()

    pp= Payment_page(driver)
    pp.payment()


    cc= Clear_cart_page(driver)
    cc.clear()














