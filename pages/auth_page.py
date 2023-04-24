from locators.elements_page_locators import AuthPageLocators
from .base_page import BasePage


class AuthPage(BasePage):

    def __init__(self, driver, timeout=10, ):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru'
        driver.maximize_window()
        driver.get(url)

        self.username = driver.find_element(*AuthPageLocators.USERNAME)
        self.password = driver.find_element(*AuthPageLocators.PASSWORD)
        self.button = driver.find_element(*AuthPageLocators.BUTTON)
        self.forgot_password = driver.find_element(*AuthPageLocators.FORGOT_PASSWORD)
        self.auth_form = driver.find_element(*AuthPageLocators.AUTH_FORM)
        self.tub_phone = driver.find_element(*AuthPageLocators.TAB_PHONE)
        self.active_tub_phone = driver.find_element(*AuthPageLocators.ACTIVE_TUB_PHONE)
        self.tub_email = driver.find_element(*AuthPageLocators.TAB_MAIL)
        self.tub_login = driver.find_element(*AuthPageLocators.TAB_LOGIN)
        self.tub_ls = driver.find_element(*AuthPageLocators.TAB_LS)
        self.register_link = driver.find_element(*AuthPageLocators.REGISTR_LINK)
        self.menu_tub = driver.find_element(*AuthPageLocators.MENU_TUB)

    def find_other_element(self, by, location):
        return self.driver.find_element(by, location)

