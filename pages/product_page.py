from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        # self.solve_quiz_and_get_code()
        self.should_be_alert_product_name_in_basket()
        self.should_be_alert_basket_price()

    def should_be_alert_product_name_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET_ALERT).text
        assert product_name == product_name_in_basket, "Wrong product in basket"

    def should_be_alert_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_ALERT).text
        assert basket_price == product_price, "Wrong basket price"
