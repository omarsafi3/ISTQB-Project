import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage


@pytest.mark.smoke
def test_add_product_to_cart_and_verify_it_appears(driver):
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    home_page.load()
    home_page.open_first_product()
    product_page.wait_until_loaded()
    selected_product = product_page.product_name()

    product_page.add_to_cart()
    alert_text = product_page.accept_alert_and_get_text()
    assert "Product added" in alert_text

    home_page.go_to_cart()
    cart_page.wait_until_loaded()

    assert selected_product in cart_page.product_names()

