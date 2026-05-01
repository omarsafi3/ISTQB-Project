from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):
    USERNAME_INPUT = (By.ID, "sign-username")
    PASSWORD_INPUT = (By.ID, "sign-password")
    SIGNUP_BUTTON = (By.XPATH, "//button[text()='Sign up']")

    def signup(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SIGNUP_BUTTON)

