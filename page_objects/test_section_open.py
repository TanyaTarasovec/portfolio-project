import time
from selenium import webdriver
from page_objects.test_base_page import BasePage
from locators.test_section import Sections


class SectionPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.slivki.by/'


    def open_section(self):
        self.click_element(Sections.sections_list)
        time.sleep(5)
        self.click_element(Sections.sections_tourism)
        time.sleep(5)
        assert self.find_element(Sections.open_section_tourism)


    def open_ad(self):
        self.click_element(Sections.sections_list)
        time.sleep(5)
        self.click_element(Sections.sections_tourism)
        time.sleep(5)
        self.click_element(Sections.open_ad)
        time.sleep(5)
        assert self.find_element(Sections.ad)

