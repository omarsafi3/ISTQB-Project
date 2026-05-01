# Test Execution Summary

## Execution Context

- Date: 2026-05-01
- Application: https://www.demoblaze.com/
- Browser: Google Chrome
- Automation stack: Python, Selenium WebDriver, pytest, pytest-html

## Functional Regression Execution

Command:

```bash
pytest tests/test_signup.py tests/test_login.py tests/test_products.py tests/test_cart.py tests/test_checkout.py tests/test_contact.py
```

Observed result from execution:

- Total tests collected: 9
- Passed: 9
- Failed: 0

Covered scenarios:

- Add product to cart and verify it appears
- Place order with valid data
- Checkout with missing required fields
- Send contact form message
- Valid login and logout
- Invalid login
- Open product details page
- Browse products by category
- Sign up with unique username

## Exploratory Bug Execution

Command:

```bash
pytest tests/test_exploratory_bugs.py
```

Observed result from execution:

- Total tests collected: 4
- Passed: 0
- Failed: 4

Interpretation:

These tests are written with the expected correct behavior. Their failure means the application accepted invalid data, so the failures reveal real validation defects.

Detected bugs:

- BUG-001: Contact form accepts empty fields
- BUG-002: Contact form accepts invalid email format
- BUG-003: Checkout accepts non-numeric credit card value
- BUG-004: Checkout allows purchase with empty cart

## Reports

## Final Complete Suite Execution

Command:

```bash
pytest --html=reports/full_test_report.html --self-contained-html
```

Expected result from complete execution:

- Total tests collected: 13
- Passed: 9 functional tests
- Failed: 4 exploratory negative tests

This full execution includes the functional regression tests and the exploratory negative tests. The 4 failing negative tests are expected in the context of bug detection because they reveal defects.

## Report Files

Recommended report generation commands:

```bash
pytest --html=reports/full_test_report.html --self-contained-html
pytest tests/test_signup.py tests/test_login.py tests/test_products.py tests/test_cart.py tests/test_checkout.py tests/test_contact.py --html=reports/functional_tests_report.html --self-contained-html
pytest tests/test_exploratory_bugs.py --html=reports/exploratory_bugs_report.html --self-contained-html
```

Expected report files:

- `reports/full_test_report.html`
- `reports/functional_tests_report.html`
- `reports/exploratory_bugs_report.html`

Generated bug evidence screenshots:

- `reports/screenshots/BUG-001-contact-empty-fields.png`
- `reports/screenshots/BUG-002-contact-invalid-email.png`
- `reports/screenshots/BUG-003-checkout-invalid-card.png`
- `reports/screenshots/BUG-004-empty-cart-checkout.png`
