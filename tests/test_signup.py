import pytest

from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.test_data import SIGNUP_PASSWORD, unique_username


@pytest.mark.smoke
def test_signup_with_unique_username(driver):
    home_page = HomePage(driver)
    signup_page = SignupPage(driver)
    username = unique_username()

    home_page.load()
    home_page.open_signup_modal()
    signup_page.signup(username, SIGNUP_PASSWORD)

    alert_text = signup_page.accept_alert_and_get_text()
    assert "Sign up successful" in alert_text

