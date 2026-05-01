import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from utils.test_data import CHECKOUT_VALID_DATA


def add_first_product_to_cart(driver):
    home_page = HomePage(driver)
    product_page = ProductPage(driver)

    home_page.load()
    home_page.open_first_product()
    product_page.wait_until_loaded()
    product_page.add_to_cart()
    product_page.accept_alert()
    home_page.go_to_cart()


@pytest.mark.smoke
def test_place_order_with_valid_data(driver):
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    add_first_product_to_cart(driver)
    cart_page.wait_until_loaded()
    cart_page.place_order()

    checkout_page.fill_order_form(CHECKOUT_VALID_DATA)
    checkout_page.submit_order()

    confirmation = checkout_page.confirmation_message()
    assert "Id:" in confirmation
    assert "Amount:" in confirmation
    assert CHECKOUT_VALID_DATA["name"] in confirmation


@pytest.mark.negative
def test_checkout_with_missing_required_fields_shows_alert(driver):
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    add_first_product_to_cart(driver)
    cart_page.wait_until_loaded()
    cart_page.place_order()
    checkout_page.submit_order()

    alert_text = checkout_page.accept_alert_and_get_text()
    assert "Please fill out Name and Creditcard" in alert_text

