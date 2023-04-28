from page_objects.test_city_select import CitySelect
import allure


@allure.title('City select')
def test_city(browser):
    with allure.step('Open city field'):
        city = CitySelect(browser)
        city.check_menu_city()

    with allure.step('Availability search city field'):
        city.check_search_city()

    with allure.step('Search city'):
        city.check_search_city()