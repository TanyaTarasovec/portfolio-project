import time
from selenium import webdriver
from page_objects.base_page import BasePage
from locators.test_language_change import LanguageChange


class languagePage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.slivki.by/'


    def check_button_language(self):
        assert self.find_element(LanguageChange.button_language).is_displayed()


    def change(self):
        self.click_element(LanguageChange.button_language)
        self.click_element(LanguageChange.polish_language)
        time.sleep(5)
        webdriver.refresh()