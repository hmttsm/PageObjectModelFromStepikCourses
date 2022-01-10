# running param: -v -rx --tb=line --language=en
import pytest
from pages.product_page import ProductPage


promo_offers = ["offer0", "offer1", "offer2", "offer3", "offer4",
                "offer5", "offer6",
                pytest.param("offer7", marks=pytest.mark.xfail(reason="Won't finish")),
                "offer8", "offer9"]


@pytest.mark.parametrize('promo_offer', promo_offers)
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_alert_should_appear()
    page.is_correct_product()
    page.price_alert_should_appear()
    page.is_correct_price()


@pytest.mark.skip(reason="according to the 4.3.6: \n"
                         "Важно! ... те тесты, которые упали пометьте как XFail или skip...")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # Добавляем товар в корзину
    page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью  is_not_element_present
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.skip(reason="according to the 4.3.6: \n"
                         "Важно! ... те тесты, которые упали пометьте как XFail или skip...")
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # Добавляем товар в корзину
    page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.success_message_should_disappear()
