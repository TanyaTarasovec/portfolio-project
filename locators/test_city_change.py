from selenium.webdriver.common.by import By


class CityChange:
    select_city_in_list = (By.CSS_SELECTOR, '[href="https://vitebsk.slivki.by"]')
    city_search_field = (By.CSS_SELECTOR, '[id="citySearchInput"]')
    select_list = (By.CSS_SELECTOR, '[class="city-selector"]')
    input_city = (By.CSS_SELECTOR, '[id="citySearchInput"]')
    delete_text = (By.CSS_SELECTOR, 'class="slivki-icon-close-circled-o"')
    enter_text_city = (By.CSS_SELECTOR, 'class="city-selector-list"')
    menu = (By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/a')
    open_profile = (By.CSS_SELECTOR, '[class="slivki-icon-menu text-black"]')
    profile = (By.CSS_SELECTOR, '[class="foodcort-d-none"]')
