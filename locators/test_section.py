from selenium.webdriver.common.by import By


class Sections:
    sections_list = (By.CSS_SELECTOR, '[data-target="#promocodeMenuContent"]')
    sections_tourism = (By.CSS_SELECTOR, '//*[@id="categoryBox14"]/ul/li[5]/a')
    open_section_tourism = (By.XPATH, '//*[@id="categoryBox5045"]/ul[1]/li[2]/a')
    open_ad = (By.XPATH, '//*[@id="action291036"]/div[5]/div/a')
    ad = (By.XPATH, '//*[@id="contentContainer"]/div/div/div/div/h3')