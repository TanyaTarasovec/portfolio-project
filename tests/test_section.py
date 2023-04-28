from page_objects.test_section_open import SectionPage
import allure


@allure.title('Sections')
def test_section(browser):
    with allure.step('Open section'):
        section = SectionPage(browser)
        section.open_section()

    with allure.step('Open ad'):
        section.open_ad()

    with allure.step('Button promokod'):
        section.button_promokod()

    with allure.step('Get promokod'):
        section.get_promokod()

    with allure.step('Sub'):
        section.subs()

    with allure.step('Checkbox'):
        section.checkbox()

    with allure.step('Disable button'):
        section.disable_button()

    with allure.step('Button_menu'):
        section.button_menu()

    with allure.step('Post action'):
        section.new_action()

    with allure.step('Message form'):
        section.message_place_form()
