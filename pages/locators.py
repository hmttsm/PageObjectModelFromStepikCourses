from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, ".content>#content_inner>p")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PAS_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_ADDED_ALERT = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)")
    PRODUCT_IN_ALERT = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")
    ACTUAL_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_ALERT = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3)")
    ACTUAL_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_ALERT = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_page")
