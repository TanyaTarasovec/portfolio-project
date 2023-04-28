from page_objects.test_language_select import languagePage
import allure


@allure.title('Language select')
def test_language(browser):
    with allure.step('Availability language button'):
        language = languagePage(browser)
        language.check_button_language()

    with allure.step('Change language'):
        language.change()