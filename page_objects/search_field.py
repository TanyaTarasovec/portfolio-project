
from selenium import webdriver
from selenium.webdriver import Keys
from page_objects.base_page import BasePage
from locators.test_search import Search


class SearchField(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.slivki.by/'


    def check_search(self):
        assert self.find_element(Search.field_search).is_displayed()


    def search(self):
        self.send_keys(Search.field_search, 'туризм')
        self.click_element(Search.button_search)
        self.send_keys(Keys.RETURN)


    def check_message(self):
        self.click_element(Search.field_search)
        self.click_element(Search.button_search)
        message_text = self.find_element(Search.message).text
        assert message_text == 'По запросу ничего не найдено'