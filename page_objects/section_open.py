import time
from selenium import webdriver
from page_objects.base_page import BasePage
from locators.test_section import Sections


class SectionPage(BasePage):
    def __init__(self, execute_script, driver: webdriver.Chrome):
        super().__init__(driver)
        self.execute_script = execute_script
        self.url = 'https://www.slivki.by/'


    def open_section(self):
        self.click_element(Sections.sections_list)
        time.sleep(5)
        self.execute_script('window.scrollTo(0, 500)')
        self.click_element(Sections.sections_tourism)
        time.sleep(5)
        assert self.find_element(Sections.open_section_tourism)


    def open_ad(self):
        self.click_element(Sections.sections_list)
        time.sleep(5)
        self.execute_script('window.scrollTo(0, 500)')
        self.click_element(Sections.sections_tourism)
        time.sleep(5)
        self.click_element(Sections.open_ad)
        time.sleep(5)
        assert self.find_element(Sections.ad)


    def button_promokod(self):
        self.find_element(Sections.button_get_promokod).is_displayed()


    def get_promokod(self):
        self.click_element(Sections.sections_list)
        time.sleep(5)
        self.execute_script('window.scrollTo(0, 500)')
        self.click_element(Sections.sections_tourism)
        time.sleep(5)
        self.click_element(Sections.open_ad)
        time.sleep(5)
        self.click_element(Sections.button_get_promokod)
        time.sleep(5)
        self.click_element(Sections.button_pay)
        self.click_element(Sections.payment_method_erip)
        self.find_element(Sections.message_order_number).is_displayed()


    def subs(self):
        self.find_element(Sections.subs).is_displayed()


    def checkbox(self):
        self.find_element(Sections.checkbox_subs_page).is_displayed()


    def disable_button(self):
        self.click_element(Sections.subs)
        self.click_element(Sections.checkbox_subs_page)
        self.find_element(Sections.checkbox_subs_page).isdisabled()
        self.find_element(Sections.button_sub).isdisabled()


    def button_menu(self):
        self.find_element(Sections.button_menu).is_displayed()


    def new_action(self):
        self.click_element(Sections.button_menu)
        self.click_element(Sections.place_share)
        self.send_keys(Sections.place_share_phone, '297350282')
        self.send_keys(Sections.place_share_email, 'tanya@mail.com')
        self.send_keys(Sections.place_share_action, 'enter message')
        self.click_element(Sections.button_send_place_share)


    def message_place_form(self):
        self.click_element(Sections.button_menu)
        self.click_element(Sections.place_share)
        self.click_element(Sections.button_send_place_share)
        self.find_element(Sections.message_place_form).is_displayed()



