from selenium import webdriver
from selenium.webdriver import Keys
from page_object.base_page import Base_Page
from locators.search import search


class search_field(Base_Page):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.slivki.by/'


#проверка наличия поля поиск

    def check_search(self):
        assert self.find_element(search.field_search).is_displayed()


#поиск

    def search(self):
        self.send_keys(search.field_search, 'туризм')
        self.click_element(search.button_search)
        self.send_keys(Keys.RETURN)


#наличие текста при отправке пустого поля поиска

    def check_message(self):
        self.click_element(search.field_search)
        self.click_element(search.button_search)
        message_text = self.find_element(search.message).text
        assert message_text == 'По запросу ничего не найдено'