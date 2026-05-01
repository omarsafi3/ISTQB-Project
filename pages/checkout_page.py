from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[text()='Purchase']")
    CONFIRMATION_MODAL = (By.CSS_SELECTOR, ".sweet-alert")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, ".sweet-alert p")
    OK_BUTTON = (By.CSS_SELECTOR, ".confirm")

    def fill_order_form(self, data):
        self.type(self.NAME_INPUT, data["name"])
        self.type(self.COUNTRY_INPUT, data["country"])
        self.type(self.CITY_INPUT, data["city"])
        self.type(self.CARD_INPUT, data["card"])
        self.type(self.MONTH_INPUT, data["month"])
        self.type(self.YEAR_INPUT, data["year"])

    def submit_order(self):
        self.click(self.PURCHASE_BUTTON)

    def confirmation_message(self):
        self.wait.until(EC.visibility_of_element_located(self.CONFIRMATION_MODAL))
        return self.get_text(self.CONFIRMATION_TEXT)

    def close_confirmation(self):
        self.click(self.OK_BUTTON)

