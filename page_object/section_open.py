import time
from selenium import webdriver
from page_object.base_page import Base_Page
from locators.sections import sections


class section_page(Base_Page):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.slivki.by/'


   #проверка открытия конкретного раздела

    def open_section(self):
        self.click_element(sections.sections_list)
        time.sleep(5)
        self.click_element(sections.sections_tourism)
        time.sleep(5)
        assert self.find_element(sections.open_section_tourism)


    #проверка открытия объявления
    def open_section(self):
        self.click_element(sections.sections_list)
        time.sleep(5)
        self.click_element(sections.sections_tourism)
        time.sleep(5)
        self.click_element(sections.open_ad)
        time.sleep(5)
        assert self.find_element(sections.ad)

