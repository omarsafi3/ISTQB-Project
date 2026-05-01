from datetime import datetime
import random


BASE_URL = "https://www.demoblaze.com/"

# DemoBlaze provides this public demo account.
VALID_USERNAME = "test"
VALID_PASSWORD = "test"

INVALID_USERNAME = "invalid_user_for_istqb_project"
INVALID_PASSWORD = "wrong_password"


def unique_username(prefix="student"):
    """Generate a new username to avoid duplicate signup data."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    suffix = random.randint(1000, 9999)
    return f"{prefix}_{timestamp}_{suffix}"


SIGNUP_PASSWORD = "Password123"

CHECKOUT_VALID_DATA = {
    "name": "ISTQB Student",
    "country": "Tunisia",
    "city": "Tunis",
    "card": "4111111111111111",
    "month": "05",
    "year": "2026",
}

CONTACT_MESSAGE = {
    "email": "student@example.com",
    "name": "ISTQB Student",
    "message": "This is a Selenium contact form test for a university project.",
}

