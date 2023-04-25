from selenium import webdriver
from page_object.base_page import Base_Page
from locators.login_page import login_page_locator


class test_profile(Base_Page):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.slivki.by/'

        #наличие кнопки "вход" на главной странице

    def check_login_for_pending(self):
        assert self.find_element(login_page_locator.button_login).is_displayed()

#налиличие полей

    def check_open_email(self):
        assert self.find_element(login_page_locator.login_by_phone).is_displayed()

    def check_login_field(self):
        assert self.find_element(login_page_locator.email_input).is_displayed()

    def check_password_field(self):
        assert self.find_element(login_page_locator.password_input).is_displayed()

    def check_checkbox(self):
        assert self.find_element(login_page_locator.checkbox_user_agreement).is_displayed()

    def button_login(self):
        assert self.find_element(login_page_locator.button_login_after).is_displayed()

        #вход в личный кабинет email

    def checking_personal_account_email(self):
        self.click_element(login_page_locator.button_login)
        self.click_element(login_page_locator.login_by_email)
        self.send_keys(login_page_locator.email_input, 'tanyatarasovec300197@gmail.com')
        self.send_keys(login_page_locator.password_input, '123Tanya')
        self.click_element(login_page_locator.checkbox_user_agreement)
        self.click_element(login_page_locator.button_login_after)
        assert self.click_element(login_page_locator.open_profile_autorization)

      #наличие ошибки при неверном вводе email

    def email_error(self):
        self.click_element(login_page_locator.button_login)
        self.click_element(login_page_locator.login_by_email)
        self.send_keys(login_page_locator.email_input, 'tanyatarasovec@gmail.com')
        self.send_keys(login_page_locator.password_input, '123Tanya')
        self.click_element(login_page_locator.button_login_after)
        error = self.find_element(login_page_locator.message_error_email)
        assert error.text == 'Неверное имя пользователя и/или пароль'
        assert error.is_displayed()

     #наличие ошибки при неверном вводе пароля

    def password_error(self):
        self.click_element(login_page_locator.button_login)
        self.click_element(login_page_locator.login_by_email)
        self.send_keys(login_page_locator.email_input, 'tanyatarasovec300197@gmail.com')
        self.send_keys(login_page_locator.password_input, '123321')
        self.click_element(login_page_locator.button_login_after)
        error = self.find_element(login_page_locator.message_error_email)
        assert error.text == 'Неверное имя пользователя и/или пароль'
        assert error.is_displayed()

