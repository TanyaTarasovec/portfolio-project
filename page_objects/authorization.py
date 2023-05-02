import time

from selenium import webdriver
from page_objects.base_page import BasePage
from locators.test_login_page import LoginPageLocator


class TestProfile(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.slivki.by/'


    def test_check_login_for_pending(self):
        assert self.find_element(LoginPageLocator.button_login).is_displayed()


    def test_check_open_email(self):
        assert self.find_element(LoginPageLocator.login_by_phone).is_displayed()

    def test_check_login_field(self):
        assert self.find_element(LoginPageLocator.email_input).is_displayed()

    def test_check_password_field(self):
        assert self.find_element(LoginPageLocator.password_input).is_displayed()

    def check_checkbox(self):
        assert self.find_element(LoginPageLocator.checkbox_user_agreement).is_displayed()

    def button_login(self):
        assert self.find_element(LoginPageLocator.button_login_after).is_displayed()


    def checking_personal_account_email(self):
        self.click_element(LoginPageLocator.button_login)
        self.click_element(LoginPageLocator.login_by_email)
        self.send_keys(LoginPageLocator.email_input, 'tanyatarasovec300197@gmail.com')
        self.send_keys(LoginPageLocator.password_input, '123Tanya')
        self.click_element(LoginPageLocator.checkbox_user_agreement)
        self.click_element(LoginPageLocator.button_login_after)
        assert self.click_element(LoginPageLocator.open_profile_autorization)


    def email_error(self):
        self.click_element(LoginPageLocator.button_login)
        self.click_element(LoginPageLocator.login_by_email)
        self.send_keys(LoginPageLocator.email_input, 'tanyatarasovec@gmail.com')
        self.send_keys(LoginPageLocator.password_input, '123Tanya')
        self.click_element(LoginPageLocator.button_login_after)
        error = self.find_element(LoginPageLocator.message_error_email)
        assert error.text == 'Неверное имя пользователя и/или пароль'
        assert error.is_displayed()


    def password_error(self):
        self.click_element(LoginPageLocator.button_login)
        self.click_element(LoginPageLocator.login_by_email)
        self.send_keys(LoginPageLocator.email_input, 'tanyatarasovec300197@gmail.com')
        self.send_keys(LoginPageLocator.password_input, '123321')
        self.click_element(LoginPageLocator.button_login_after)
        error = self.find_element(LoginPageLocator.message_error_email)
        assert error.text == 'Неверное имя пользователя и/или пароль'
        assert error.is_displayed()


    def logaut(self):
        self.click_element(LoginPageLocator.button_login)
        self.click_element(LoginPageLocator.login_by_email)
        self.send_keys(LoginPageLocator.email_input, 'tanyatarasovec300197@gmail.com')
        self.send_keys(LoginPageLocator.password_input, '123Tanya')
        self.click_element(LoginPageLocator.checkbox_user_agreement)
        self.click_element(LoginPageLocator.button_login_after)
        time.sleep(5)
        self.click_element(LoginPageLocator.button_menu)
        self.click_element(LoginPageLocator.button_logaut)
        self.find_element(LoginPageLocator.popup_logaut).is_displayed()
        self.click_element(LoginPageLocator.button_popup_logaut)
        time.sleep(5)
