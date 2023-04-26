from page_objects.test_authorization import TestProfile
from page_objects.test_city_select import CitySelect
from page_objects.test_search_field import SearchField
from page_objects.test_section_open import SectionPage
from page_objects.test_language_select import languagePage


def test_slivki(browser):
    authorization = TestProfile(browser)
    authorization.open()

    authorization.test_check_login_for_pending()

    authorization.test_check_open_email()

    authorization.test_check_login_field()

    authorization.test_check_password_field()

    authorization.check_checkbox()

    authorization.button_login()

    authorization.checking_personal_account_email()

    authorization.email_error()

    authorization.password_error()

    city = CitySelect(browser)

    city.check_menu_city()

    city.check_search_city()

    language = languagePage(browser)

    language.check_button_language()

    language.change()

    search = SearchField(browser)

    search.check_search()

    search.search()

    search.check_message()

    section = SectionPage(browser)

    section.open_section()

    section.open_ad()


