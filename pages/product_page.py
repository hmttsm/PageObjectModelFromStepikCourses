from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "There is no add to basket button"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def product_alert_should_appear(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_ALERT), "There is no PRODUCT(added) ALERT"

    def is_correct_product(self):
        current_book = self.browser.find_element(*ProductPageLocators.ACTUAL_PRODUCT).text
        book_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_ALERT).text
        assert current_book == book_in_alert, "OOPS, books are different"

    def price_alert_should_appear(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_ALERT), "There is no PRICE ALERT"

    def is_correct_price(self):
        current_price = self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.PRICE_IN_ALERT).text
        assert current_price == price_in_alert, "OOPS, prices are different"
