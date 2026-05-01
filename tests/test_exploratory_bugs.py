import pytest
from pathlib import Path

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from utils.test_data import CHECKOUT_VALID_DATA


EVIDENCE_DIR = Path(__file__).resolve().parents[1] / "reports" / "screenshots"


def save_evidence(driver, filename):
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    driver.save_screenshot(str(EVIDENCE_DIR / filename))


@pytest.mark.negative
def test_contact_empty_fields_should_be_rejected(driver):
    """Defect-revealing test: contact form should reject empty data."""
    home_page = HomePage(driver)

    home_page.load()
    home_page.send_contact_message("", "", "")

    alert_text = home_page.accept_alert_and_get_text()
    save_evidence(driver, "BUG-001-contact-empty-fields.png")
    assert "Thanks for the message" not in alert_text


@pytest.mark.negative
def test_contact_invalid_email_should_be_rejected(driver):
    """Defect-revealing test: invalid email format should be rejected."""
    home_page = HomePage(driver)

    home_page.load()
    home_page.send_contact_message(
        "not-an-email",
        "ISTQB Student",
        "Testing invalid email validation.",
    )

    alert_text = home_page.accept_alert_and_get_text()
    save_evidence(driver, "BUG-002-contact-invalid-email.png")
    assert "Thanks for the message" not in alert_text


@pytest.mark.negative
def test_checkout_non_numeric_card_should_be_rejected(driver):
    """Defect-revealing test: card field should reject non-numeric text."""
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    home_page.load()
    home_page.open_first_product()
    product_page.wait_until_loaded()
    product_page.add_to_cart()
    product_page.accept_alert()
    home_page.go_to_cart()
    cart_page.wait_until_loaded()
    cart_page.place_order()

    invalid_card_data = CHECKOUT_VALID_DATA.copy()
    invalid_card_data["card"] = "abcd"
    checkout_page.fill_order_form(invalid_card_data)
    checkout_page.submit_order()

    confirmation = checkout_page.confirmation_message()
    save_evidence(driver, "BUG-003-checkout-invalid-card.png")
    assert "Id:" not in confirmation


@pytest.mark.negative
def test_checkout_empty_cart_should_be_rejected(driver):
    """Defect-revealing test: checkout should require at least one cart item."""
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    home_page.load()
    home_page.go_to_cart()
    cart_page.wait_until_loaded()
    cart_page.place_order()
    checkout_page.fill_order_form(CHECKOUT_VALID_DATA)
    checkout_page.submit_order()

    confirmation = checkout_page.confirmation_message()
    save_evidence(driver, "BUG-004-empty-cart-checkout.png")
    assert "Id:" not in confirmation
