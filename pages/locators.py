from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span>a.btn-default[href*='basket']")


class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
    EMPTY_BASKET = (By.CSS_SELECTOR, "div#content_inner>p")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "id_registration-password1")
    REGISTER_PASSWORD_REPEAT_FIELD = (By.CSS_SELECTOR, "id_registration-password2")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_NAME_IN_BASKET_ALERT = (By.CSS_SELECTOR, "#messages>.alert:first-child .alertinner strong")
    BASKET_PRICE_ALERT = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3) .alertinner strong")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert-success:first-child")
