from selenium.webdriver.common.by import By


class LoginPageLocator:
    button_login = (By.CSS_SELECTOR, '[class="enter focus-tel login-button"]')
    login_by_email = (By.CSS_SELECTOR, '[data-target="#loginMail"]')
    email_input = (By.CSS_SELECTOR, '[style="font-size: 20px"][class="form-element"]')
    password_input = (By.CSS_SELECTOR, '[class="form-element mb-2"]')
    checkbox_user_agreement = (By.XPATH, '//label[@for="termsOfUse_email"]')
    button_login_after = (By.CSS_SELECTOR, 'id="loginSendCodeButton"')
    message_not_checkbox = (By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/label')
    message_error_email = (By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/label')
    login_by_phone = (By.XPATH, '//*[@id="loginForm"]/div[2]/a')
    phone_input = (By.CSS_SELECTOR, '[id="loginPhoneInput"]')
    message_not_input = (By.XPATH, '/html/body/div[11]/div/div/div[2]/div/div/form/div[1]/div/label')
    open_profile_autorization = (By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/ul/li[1]/a[1]')
    button_menu = (By.CSS_SELECTOR, '[id="header-profile-menu-opener"]')
    button_logaut = (By.CSS_SELECTOR, '[class="item-logout"]')
    popup_logaut = (By.XPATH, '//*[@id="logoutConfirmPopup"]/div/div')
    button_popup_logaut = (By.CSS_SELECTOR, '[href="/profile/logout"]')
