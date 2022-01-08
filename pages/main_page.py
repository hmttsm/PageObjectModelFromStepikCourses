from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # https://stepik.org/lesson/238819/step/9?unit=211271 (переходы между страницами)
        # Первый способ: возвращать нужный Page Object.
