from locators.elements_page_locators import AuthPageLocators, RegPageLocators
from pages.base_page import BasePage


class RegistrPage(BasePage):

    def __init__(self, driver, timeout=10, ):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru/'
        driver.get(url)
        driver.find_element(*AuthPageLocators.REGISTR_LINK).click()

        self.first_name = driver.find_element(*RegPageLocators.FIRST_NAME)
        self.last_name = driver.find_element(*RegPageLocators.LAST_NAME)
        self.region_selection = driver.find_element(*RegPageLocators.REGION_SELECTION)
        self.email_registration = driver.find_element(*RegPageLocators.EMAIL_OR_PHONE)
        self.password = driver.find_element(*RegPageLocators.PASSWORD)
        self.password_confirm = driver.find_element(*RegPageLocators.PASSWORD_CONFIRM)
        self.button_reg = driver.find_element(*RegPageLocators.BUTTON_REG)
        self.page_left = driver.find_element(*RegPageLocators.PAGE_LEFT_REGISTRATION)
        self.auth_form = driver.find_element(*AuthPageLocators.AUTH_FORM)
        self.container_first_name = driver.find_element(*RegPageLocators.CONTAINER_FIRST_NAME)
        self.container_last_name = driver.find_element(*RegPageLocators.CONTAINER_LAST_NAME)
        self.container_password_confirm = driver.find_element(*RegPageLocators.PASSWORD_CONFIRM)

    def find_other_element(self, by, location):
        return self.driver.find_element(by, location)