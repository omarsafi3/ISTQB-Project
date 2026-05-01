import pytest

from pages.home_page import HomePage
from pages.product_page import ProductPage


@pytest.mark.smoke
def test_open_product_details_page(driver):
    home_page = HomePage(driver)
    product_page = ProductPage(driver)

    home_page.load()
    product_names = home_page.product_names()
    home_page.open_first_product()
    product_page.wait_until_loaded()

    assert product_page.product_name() in product_names
    assert "$" in product_page.product_price()


def test_browse_products_by_category(driver):
    home_page = HomePage(driver)

    home_page.load()
    home_page.select_category("Laptops")

    product_names = home_page.product_names()
    assert len(product_names) > 0

