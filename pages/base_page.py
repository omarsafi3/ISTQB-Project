import os
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


PRESENTATION_DELAY = float(os.getenv("PRESENTATION_DELAY", "0.7"))


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def pause_for_presentation(self):
        """Small optional delay so Selenium actions are visible during demos."""
        if PRESENTATION_DELAY > 0:
            time.sleep(PRESENTATION_DELAY)

    def open(self, url):
        self.driver.get(url)
        self.pause_for_presentation()

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        self.pause_for_presentation()

    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        self.pause_for_presentation()

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

    def wait_for_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        return alert.text

    def accept_alert(self):
        self.wait.until(EC.alert_is_present())
        Alert(self.driver).accept()
        self.pause_for_presentation()

    def accept_alert_and_get_text(self):
        text = self.wait_for_alert_text()
        self.accept_alert()
        return text
