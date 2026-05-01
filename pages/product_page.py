from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, ".name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price-container")
    ADD_TO_CART_BUTTON = (By.LINK_TEXT, "Add to cart")

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME))

    def product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def product_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

