from page_objects.test_authorization import TestProfile
from page_objects.test_city_select import CitySelect
from page_objects.test_search_field import SearchField
from page_objects.test_section_open import SectionPage
from page_objects.test_language_select import languagePage
import allure


@allure.title('Open home page and authorization')
def test_authorization(browser):
    with allure.step('Display button login'):
        authorization = TestProfile(browser)
        authorization.test_check_login_for_pending()

    with allure.step('Availability Login by email fields on the page'):
        authorization.test_check_open_email()

    with allure.step('Availability Email fields on the page'):
        authorization.test_check_login_field()

    with allure.step('Availability Password fields on the page'):
        authorization.test_check_password_field()

    with allure.step('Availability Checkbox on the page'):
        authorization.check_checkbox()

    with allure.step('Availability button login on the page'):
        authorization.button_login()

    with allure.step('Login in account'):
        authorization.checking_personal_account_email()

    with allure.step('Message error email'):
        authorization.email_error('Неверное имя пользователя и/или пароль')

    with allure.step('Message error password'):
        authorization.password_error('Неверное имя пользователя и/или пароль')


@allure.title('City select')
def test_city(browser):
    with allure.step('Open city field'):
        city = CitySelect(browser)
        city.check_menu_city()

    with allure.step('Availability search city field'):
        city.check_search_city()

    with allure.step('Search city'):
        city.check_search_city()


@allure.title('Language select')
def test_language(browser):
    with allure.step('Availability language button'):
        language = languagePage(browser)
        language.check_button_language()

    with allure.step('Change language'):
        language.change()


@allure.title('Search field')
def test_search(browser):
    with allure.step('Availability search field'):
        search = SearchField(browser)
        search.check_search()

    with allure.step('Search'):
        search.search()

    with allure.step('Message field'):
        search.check_message('По запросу ничего не найдено')


@allure.title('Sections')
def test_section(browser):
    with allure.step('Open section'):
        section = SectionPage(browser)
        section.open_section()

    with allure.step('Open ad'):
        section.open_ad()
