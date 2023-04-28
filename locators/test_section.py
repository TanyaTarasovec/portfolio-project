from selenium.webdriver.common.by import By


class Sections:
    sections_list = (By.CSS_SELECTOR, '[data-target="#promocodeMenuContent"]')
    sections_tourism = (By.CSS_SELECTOR, '//*[@id="categoryBox14"]/ul/li[5]/a')
    open_section_tourism = (By.XPATH, '//*[@id="categoryBox5045"]/ul[1]/li[2]/a')
    open_ad = (By.XPATH, '//*[@id="action291036"]/div[5]/div/a')
    ad = (By.XPATH, '//*[@id="contentContainer"]/div/div/div/div/h3')
    button_get_promokod = (By.XPATH, '//*[@id="buyCodeButton"]')
    button_pay = (By.CSS_SELECTOR, '[id="offerAcceptButton"]')
    payment_method_erip = (By.CSS_SELECTOR, '[onclick="ym(20933521,"reachGoal","buycode-erip");"]')
    message_order_number = (By.XPATH, '//*[@id="raschet"]/p[1]/text()[1]')
    subs = (By.CSS_SELECTOR, '[href="/profile/subscription/manage?utm_source=main_menu"]')
    checkbox_subs_page = (By.XPATH, '//*[@id="subscriptionTab"]/div[2]/div[1]/div/label')
    button_sub = (By.XPATH, '//*[@id="subscriptionTab"]/div[2]/div[2]/div[1]/div/div[2]/a')
    button_menu = (By.CSS_SELECTOR, '[id="header-profile-menu-opener"]')
    place_share = (By.CSS_SELECTOR, '[class="item-own-offer"]')
    place_share_phone = (By.CSS_SELECTOR, '[name="offerPhone"]')
    place_share_email = (By.CSS_SELECTOR, '[name="offerEmail"]')
    place_share_action = (By.CSS_SELECTOR, '[name="termsOfPromotion"]')
    button_send_place_share = (By.CSS_SELECTOR, '[class="btn btn-block bg-slivki text-white"]')
    message_place_form = (By.CSS_SELECTOR, '[id="createOwnOfferFormError"]')





