import time
from selenium import webdriver
from page_object.base_page import Base_Page
from locators.language_change import language_change


class language_page(Base_Page):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.slivki.by/'


   #отображение кнопки языка
    def check_button_language(self):
        assert self.find_element(language_change.button_language).is_displayed()


#изменить язык страницы
    def change(self):
        self.click_element(language_change.button_language)
        self.click_element(language_change.polish_language)
        time.sleep(5)
        webdriver.refresh()