from selenium.webdriver.common.by import By


class Search:
    field_search = (By.CSS_SELECTOR, '[id="headerSearchInput"]')
    button_search = (By.CSS_SELECTOR, '[class="input-group-append button-search-landing"]')
    message = (By.XPATH, '//*[@id="contentContainer"]/div/div/div/h1')


