import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.test_data import (
    INVALID_PASSWORD,
    INVALID_USERNAME,
    SIGNUP_PASSWORD,
    unique_username,
)


@pytest.mark.smoke
def test_valid_login_and_logout(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    signup_page = SignupPage(driver)
    username = unique_username("login_user")

    home_page.load()
    home_page.open_signup_modal()
    signup_page.signup(username, SIGNUP_PASSWORD)
    signup_page.accept_alert()

    # Reloading keeps the login test simple after the signup modal closes.
    home_page.load()
    home_page.open_login_modal()
    login_page.login(username, SIGNUP_PASSWORD)

    assert username in home_page.logged_in_username()

    home_page.logout()
    assert home_page.is_visible(HomePage.LOGIN_LINK)


@pytest.mark.negative
def test_invalid_login_shows_error_alert(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.load()
    home_page.open_login_modal()
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    alert_text = login_page.accept_alert_and_get_text()
    assert alert_text in ["User does not exist.", "Wrong password."]
