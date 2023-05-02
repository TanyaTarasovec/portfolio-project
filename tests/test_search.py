from page_objects.search_field import SearchField
import allure


@allure.title('Search field')
def test_search(browser):
    with allure.step('Availability search field'):
        search = SearchField(browser)
        search.check_search()

    with allure.step('Search'):
        search.search()

    with allure.step('Message field'):
        search.check_message('По запросу ничего не найдено')