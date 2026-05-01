from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.test_data import BASE_URL


class HomePage(BasePage):
    SIGN_UP_LINK = (By.ID, "signin2")
    LOGIN_LINK = (By.ID, "login2")
    LOGOUT_LINK = (By.ID, "logout2")
    CART_LINK = (By.ID, "cartur")
    CONTACT_LINK = (By.LINK_TEXT, "Contact")
    WELCOME_USER = (By.ID, "nameofuser")
    PRODUCT_TITLES = (By.CSS_SELECTOR, ".card-title a")
    CATEGORIES = (By.CSS_SELECTOR, ".list-group a")
    CONTACT_EMAIL = (By.ID, "recipient-email")
    CONTACT_NAME = (By.ID, "recipient-name")
    CONTACT_MESSAGE = (By.ID, "message-text")
    SEND_MESSAGE_BUTTON = (By.XPATH, "//button[text()='Send message']")

    def load(self):
        self.open(BASE_URL)
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))

    def open_signup_modal(self):
        self.click(self.SIGN_UP_LINK)

    def open_login_modal(self):
        self.click(self.LOGIN_LINK)

    def logout(self):
        self.click(self.LOGOUT_LINK)
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_LINK))

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def open_first_product(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_TITLES)).click()

    def product_names(self):
        products = self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCT_TITLES))
        return [product.text for product in products]

    def select_category(self, category_name):
        category = (By.LINK_TEXT, category_name)
        self.click(category)
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))

    def send_contact_message(self, email, name, message):
        self.click(self.CONTACT_LINK)
        self.type(self.CONTACT_EMAIL, email)
        self.type(self.CONTACT_NAME, name)
        self.type(self.CONTACT_MESSAGE, message)
        self.click(self.SEND_MESSAGE_BUTTON)

    def logged_in_username(self):
        return self.get_text(self.WELCOME_USER)

