from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ROWS = (By.CSS_SELECTOR, "#tbodyid tr")
    PRODUCT_NAMES = (By.CSS_SELECTOR, "#tbodyid td:nth-child(2)")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Place Order']")

    def wait_until_loaded(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "tbodyid")))

    def product_names(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_ROWS))
        products = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [product.text for product in products]

    def place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)

