import pytest
from locators.elements_page_locators import AuthPageLocators, RegPageLocators
from pages.auth_page import AuthPage
from pages.registr_page import RegistrPage
from settings import Settings


# 1. Авторизация с валидными данными
def test_authorization_with_valid_data(selenium):
    page = AuthPage(selenium)
    page.username.clear()
    page.username.send_keys(Settings.valid_email)
    page.password.clear()
    page.password.send_keys(Settings.valid_password)
    page.button.click()
    assert page.find_other_element(*RegPageLocators.CREDENTIALS).text == 'Учетные данные'


# 2. Авторизация с некорректной почтой
@pytest.mark.parametrize('invalid_email', ['invalid.mailru', '@error.ru',  '123', '!!!', 'ошибочный'])

def test_authorization_with_invalid_email(selenium, invalid_email):
    page = AuthPage(selenium)
    page.username.clear()
    page.username.send_keys(invalid_email)
    page.password.clear()
    page.password.send_keys(Settings.valid_password)
    page.button.click()

    assert 'Неверный логин или пароль' in page.find_other_element(*AuthPageLocators.ERROR_MESSAGE).text


# 3. Авторизация с некорректным паролем
@pytest.mark.parametrize('invalid_password', ['123', 'abc', 'error-ошибка', '!!!', 'ошибочный'])

def test_authorization_with_invalid_password(selenium, invalid_password):
    page = AuthPage(selenium)
    page.username.clear()
    page.username.send_keys(Settings.valid_email)
    page.password.clear()
    page.password.send_keys(invalid_password)
    page.button.click()

    assert 'Неверный логин или пароль' in page.find_other_element(*AuthPageLocators.ERROR_MESSAGE).text


# 4. Соответствие название таба
def test_tab_name_check(selenium):
    page = AuthPage(selenium)
    menu = [page.tub_phone.text, page.tub_email.text, page.tub_login.text, page.tub_ls.text]
    for i in range(len(menu)):
        assert "Телефон" in menu
        assert 'Почта' in menu
        assert 'Логин' in menu
        assert 'Лицевой счёт' in menu


# 5. Основные элементы формы авторизации
def test_basic_authorization_elements(selenium):
    page = AuthPage(selenium)

    assert page.menu_tub.text in page.auth_form.text
    assert page.username.text in page.auth_form.text
    assert page.password.text in page.auth_form.text
    assert page.button.text in page.auth_form.text
    assert page.forgot_password.text in page.auth_form.text
    assert page.register_link.text in page.auth_form.text


# 6. Меню с выбором авторизации
def test_menu_authorization(selenium):
    page = AuthPage(selenium)

    assert page.active_tub_phone.text == Settings.menu_auth[0]


# 7. Переход на страницу "Восстановлению пароля"
def test_forgot_password_link(selenium):
    page = AuthPage(selenium)
    page.driver.execute_script("arguments[0].click();", page.forgot_password)

    assert page.find_other_element(*AuthPageLocators.PASSWORD_RECOVERY).text == 'Восстановление пароля'


# 8. Переход к форме регистрации
def test_registration_link(selenium):
    page = AuthPage(selenium)
    page.register_link.click()

    assert page.find_other_element(*RegPageLocators.REGISTRATION).text == 'Регистрация'


# 9. Регистрация пользователя, который был зарегистрирован ранее
def test_re_registration(selenium):

    page = RegistrPage(selenium)
    page.first_name.clear()
    page.first_name.send_keys(Settings.first_name)
    page.last_name.clear()
    page.last_name.send_keys(Settings.last_name)
    page.email_registration.clear()
    page.email_registration.send_keys(Settings.valid_email)
    page.password.clear()
    page.password.send_keys(Settings.valid_password)
    page.password_confirm.clear()
    page.password_confirm.send_keys(Settings.valid_password)
    page.button_reg.click()

    assert "Учётная запись уже существует" in page.find_other_element(*AuthPageLocators.ERROR_ACCOUNT_EXISTS).text


# 10. Имя с допустимым количеством символов
@pytest.mark.parametrize("valid_first_name",
                         [
                             (Settings.cyrillic) * 2,
                             (Settings.cyrillic) * 13,
                             (Settings.cyrillic) * 30

                         ])
def test_name_form_validation(selenium, valid_first_name):
    page = RegistrPage(selenium)
    page.first_name.clear()
    page.first_name.send_keys(valid_first_name)
    page.button_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' not in page.container_first_name.text



# 11. Имя с недопустим значением
@pytest.mark.parametrize("invalid_first_name",
                         [
                             (Settings.cyrillic) * 1,
                             (Settings.cyrillic) * 31,
                             (Settings.cyrillic) * 100,
                             (Settings.cyrillic) * 256,
                             (Settings.empty), (Settings.numbers), (Settings.latin),
                             (Settings.chinese), (Settings.special_character)
])
def test_name_with_invalid_value(selenium, invalid_first_name):

    page = RegistrPage(selenium)
    page.first_name.clear()
    page.first_name.send_keys(invalid_first_name)
    page.button_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in \
           page.find_other_element(*AuthPageLocators.ERROR_FIRST_NAME).text


# 12. Фамилия  с допустимым количеством символов
@pytest.mark.parametrize("valid_last_name",
                         [
                             (Settings.cyrillic) * 2,
                             (Settings.cyrillic) * 10,
                             (Settings.cyrillic) * 30

                         ])
def test_last_name_form_validation(selenium, valid_last_name):
    page = RegistrPage(selenium)
    page.last_name.clear()
    page.last_name.send_keys(valid_last_name)
    page.button_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' not in page.container_last_name.text


# 13. Фамилия с недопустимым количеством символов
@pytest.mark.parametrize("invalid_last_name",
                         [
                             (Settings.cyrillic) * 1,
                             (Settings.cyrillic) * 31,
                             (Settings.cyrillic) * 256,
                             (Settings.empty), (Settings.numbers), (Settings.latin),
                             (Settings.chinese), (Settings.special_character)
])
def test_last_name_with_invalid_value(selenium, invalid_last_name):

    page = RegistrPage(selenium)
    page.last_name.clear()
    page.last_name.send_keys(invalid_last_name)
    page.button_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in \
           page.find_other_element(*AuthPageLocators.ERROR_LAST_NAME).text


# 14. Пароль с допустимым значением
@pytest.mark.parametrize('valid_password', ['Abc1234!', 'Abc1234!!!',  'Abc1234!!!Abc1234!!!'])
def test_password_with_valid_value(selenium, valid_password):
    page = RegistrPage(selenium)
    page.password.clear()
    page.password.send_keys(valid_password)
    page.button_reg.click()

    assert 'Длина пароля должна быть не менее 8 символов' and \
           'Длина пароля должна быть не более 20 символов' and \
           'Пароль должен содержать хотя бы одну заглавную букву' and \
           'Пароль должен содержать хотя бы одну строчную букву' and \
           'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' not in \
           page.password.text


# 15. Сравнение введеных значений: "Пароль" и "Подтверждение пароля"
def test_password_comparison(selenium):
    page = RegistrPage(selenium)
    page.password.clear()
    page.password.send_keys(Settings.valid_password)
    page.password_confirm.clear()
    page.password_confirm.send_keys(Settings.valid_password)
    page.button_reg.click()

    assert 'Пароли не совпадают' not in page.container_password_confirm.text


# 16. Сравнение введеных значений: "Пароль" и "Подтверждение пароля", которые не совпадают
def test_comparison_of_different_password(selenium):
    page = RegistrPage(selenium)
    page.password.clear()
    page.password.send_keys(Settings.valid_password)
    page.password_confirm.clear()
    page.password_confirm.send_keys(Settings.invalid_password)
    page.button_reg.click()

    assert 'Пароли не совпадают' in page.find_other_element(*AuthPageLocators.ERROR_PASSWORD_CONFIRM).text


# 17. Проверка слогана на странице регистрации
def test_tagline_check(selenium):
    try:
        page = RegistrPage(selenium)
        assert page.page_left.text != ''
    except AssertionError:
        print('Элемент отсутствует в левой части формы')


# 18. Основные элементы формы регистрации
def test_elements_registration(selenium):
    page = RegistrPage(selenium)
    form_reg = [page.first_name, page.last_name, page.region_selection, page.email_registration, page.password, page.password_confirm, page.button_reg]
    for i in range(len(form_reg)):
        assert page.first_name in form_reg
        assert page.last_name in form_reg
        assert page.region_selection in form_reg
        assert page.email_registration in form_reg
        assert page.password in form_reg
        assert page.password_confirm in form_reg
        assert page.button_reg in form_reg


# 19. Соответствие название таба в форме регистрации
def test_tab_name_registration(selenium):
    page = RegistrPage(selenium)
    assert 'Имя' in page.auth_form.text
    assert 'Фамилия' in page.auth_form.text
    assert 'Регион' in page.auth_form.text
    assert 'E-mail или мобильный телефон' in page.auth_form.text
    assert 'Пароль' in page.auth_form.text
    assert 'Подтверждение пароля' in page.auth_form.text
    assert 'Зарегистрироваться' in page.auth_form.text


# 20. Регистрация пользователя с валидными данными
def test_registration_valid_data(selenium):
    page = RegistrPage(selenium)
    page.first_name.clear()
    page.first_name.send_keys(Settings.first_name)
    page.last_name.clear()
    page.last_name.send_keys(Settings.last_name)
    page.region_selection.click()
    page.region_selection.send_keys(Settings.region_select)
    page.region_selection.click()
    # page.find_other_element(*RegPageLocators.CITY).click()
    page.email_registration.clear()
    page.email_registration.send_keys(Settings.valid_email_reg)
    page.password.clear()
    page.password.send_keys(Settings.valid_password)
    page.password_confirm.clear()
    page.password_confirm.send_keys(Settings.valid_password)
    page.button_reg.click()

    assert page.find_other_element(*AuthPageLocators.EMAIL_CONFIRM).text == 'Подтверждение email'






















