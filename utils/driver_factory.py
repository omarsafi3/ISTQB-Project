import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


SCREENSHOT_DIR = Path(__file__).resolve().parents[1] / "reports" / "screenshots"


def create_driver():
    """Create a Chrome WebDriver using Selenium Manager."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-dev-shm-usage")

    if os.getenv("HEADLESS", "").lower() in ["1", "true", "yes"]:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1366,768")

    # Selenium Manager automatically finds/downloads the matching driver.
    return webdriver.Chrome(options=chrome_options)


@pytest.fixture
def driver(request):
    browser = create_driver()
    browser.implicitly_wait(0)
    yield browser

    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
        screenshot_name = f"{request.node.name}.png"
        browser.save_screenshot(str(SCREENSHOT_DIR / screenshot_name))

    browser.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Expose test result to fixtures so screenshots can be captured on failure."""
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
