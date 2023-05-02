import time
from selenium import webdriver
from page_objects.base_page import BasePage
from locators.test_city_change import CityChange


class CitySelect(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.slivki.by/'


    def check_menu_city(self):
        assert self.find_element(CityChange.menu).is_displayed()


    def check_search_city(self):
        assert self.find_element(CityChange.city_search_field).is_displayed()


    def search_city(self):
        self.click_element(CityChange.menu)
        self.send_keys(CityChange.city_search_field, 'Витебск')
        self.click_element(CityChange.select_city_in_list)
        time.sleep(5)
        self.click_element(CityChange.open_profile)
        text = self.click_element(CityChange.profile)
        assert text.text == 'Витебск'
