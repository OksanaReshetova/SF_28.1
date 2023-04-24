from selenium.webdriver.common.by import By


class AuthPageLocators:
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    BUTTON = (By.ID, "kc-login")
    FORGOT_PASSWORD = (By.ID, "forgot_password")
    AUTH_FORM = (By.CLASS_NAME, 'card-container__wrapper')
    MENU_TUB = (By.XPATH, "//div[@class='rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs']")
    TAB_PHONE = (By.ID, 't-btn-tab-phone')
    TAB_MAIL = (By.ID, 't-btn-tab-mail')
    TAB_LOGIN = (By.ID, 't-btn-tab-login')
    TAB_LS = (By.ID, 't-btn-tab-ls')
    ACTIVE_TUB_PHONE = (By.XPATH, '//div[@id="t-btn-tab-phone" and @class="rt-tab rt-tab--small rt-tab--active"]')
    REGISTR_LINK = (By.ID, "kc-register")
    PASSWORD_RECOVERY = (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]")
    ERROR_FIRST_NAME = (By.XPATH, "//form/div[1]/div[1]/span")
    ERROR_LAST_NAME = (By.XPATH, '//form/div[1]/div[2]/span')
    ERROR_PASSWORD_CONFIRM = (By.XPATH, '//form/div[4]/div[2]/span')
    ERROR_ACCOUNT_EXISTS = (By.XPATH, '//h2[text()="Учётная запись уже существует"]')
    EMAIL_CONFIRM = (By.XPATH, "//section/div/div/h1")
    ERROR_MESSAGE = (By.XPATH, '//span[@id="form-error-message"]')


class RegPageLocators:
    CREDENTIALS = (By.XPATH, "//body/div[@id='app']/main[1]/div[1]/div[2]/div[1]/h3[1]")
    REGISTRATION = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    REGION_SELECTION = (By.XPATH, "//div[@class='rt-input-container rt-select__input']//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange']")
    CITY = (By.XPATH, "//div[13]")
    EMAIL_OR_PHONE = (By.XPATH, "//input[@id='address']")
    PASSWORD = (By.CSS_SELECTOR, '#password')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#password-confirm')
    BUTTON_REG = (By.XPATH, "//button[@name='register']")
    CONTAINER_FIRST_NAME = (By.XPATH, '//div[1][@class="rt-input-container"]')
    CONTAINER_LAST_NAME = (By.XPATH, '//div[2][@class="rt-input-container"]')
    PAGE_LEFT_REGISTRATION = (By.ID, 'page-left')