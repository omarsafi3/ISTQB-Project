import pytest

from pages.home_page import HomePage
from utils.test_data import CONTACT_MESSAGE


@pytest.mark.smoke
def test_send_contact_form_message(driver):
    home_page = HomePage(driver)

    home_page.load()
    home_page.send_contact_message(
        CONTACT_MESSAGE["email"],
        CONTACT_MESSAGE["name"],
        CONTACT_MESSAGE["message"],
    )

    alert_text = home_page.accept_alert_and_get_text()
    assert "Thanks for the message" in alert_text

