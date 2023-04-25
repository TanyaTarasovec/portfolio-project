import time
from selenium import webdriver
from page_object.base_page import Base_Page
from locators.city_change import city_change


class city_select(Base_Page):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.slivki.by/'


   #отображение кнопки городов
    def check_menu_city(self):
        assert self.find_element(city_change.menu).is_displayed()

    #отображение поля поиск
    def check_search_city(self):
        assert self.find_element(city_change.city_search_field).is_displayed()


#изменить город
    def search_city(self):
        self.click_element(city_change.menu)
        self.send_keys(city_change.city_search_field, 'Витебск')
        self.click_element(city_change.select_city_in_list)
        time.sleep(5)
        self.click_element(city_change.open_profile)
        text = self.click_element(city_change.profile)
        assert text.text == 'Витебск'
