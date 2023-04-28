from page_objects.test_authorization import TestProfile
import allure


@allure.title('Open home page and authorization')
def test_authorization(browser):
    with allure.step('Display button login'):
        authorization = TestProfile(browser)
        authorization.test_check_login_for_pending()

    with allure.step('Availability Login by email fields on the page'):
        authorization.test_check_open_email()

    with allure.step('Availability Email fields on the page'):
        authorization.test_check_login_field()

    with allure.step('Availability Password fields on the page'):
        authorization.test_check_password_field()

    with allure.step('Availability Checkbox on the page'):
        authorization.check_checkbox()

    with allure.step('Availability button login on the page'):
        authorization.button_login()

    with allure.step('Login in account'):
        authorization.checking_personal_account_email()

    with allure.step('Message error email'):
        authorization.email_error('Неверное имя пользователя и/или пароль')

    with allure.step('Message error password'):
        authorization.password_error('Неверное имя пользователя и/или пароль')

    with allure.step('Logaut'):
        authorization.logaut()
