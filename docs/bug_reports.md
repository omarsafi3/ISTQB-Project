# Bug Reports / Observations

This file is used to document verified bugs and potential observations found during testing.

Important: do not mark an item as a confirmed bug until it has been reproduced and supported with evidence such as a screenshot, test result, or manual notes.

## BUG-001 - Contact form accepts empty message

**Status:** Confirmed by failing negative test  
**Feature:** Contact form  
**Severity:** Medium  
**Priority:** Medium  
**Reproducibility:** Always during automated execution

### Description

The contact form accepts empty fields and displays a success message. A contact form should normally require at least a valid email, contact name, and message.

### Steps To Reproduce

1. Open https://www.demoblaze.com/
2. Click `Contact`.
3. Leave email, name, and message empty.
4. Click `Send message`.

### Expected Result

The application should display a validation message and should not send an empty contact request.

### Actual Result

The application displays the success alert: `Thanks for the message!!`

### Evidence

Automated negative test failed: `tests/test_exploratory_bugs.py::test_contact_empty_fields_should_be_rejected`

### Screenshot Path

`reports/screenshots/BUG-001-contact-empty-fields.png`

## BUG-002 - Contact form accepts invalid email format

**Status:** Confirmed by failing negative test  
**Feature:** Contact form  
**Severity:** Low  
**Priority:** Medium  
**Reproducibility:** Always during automated execution

### Description

The contact form accepts an invalid email format. A web form should normally reject invalid email addresses before accepting the message.

### Steps To Reproduce

1. Open https://www.demoblaze.com/
2. Click `Contact`.
3. Enter `not-an-email` in the email field.
4. Enter a valid name and message.
5. Click `Send message`.

### Expected Result

The application should reject the invalid email format.

### Actual Result

The application displays the success alert: `Thanks for the message!!`

### Evidence

Automated negative test failed: `tests/test_exploratory_bugs.py::test_contact_invalid_email_should_be_rejected`

### Screenshot Path

`reports/screenshots/BUG-002-contact-invalid-email.png`

## BUG-003 - Checkout accepts non-numeric credit card value

**Status:** Confirmed by failing negative test  
**Feature:** Checkout  
**Severity:** High  
**Priority:** High  
**Reproducibility:** Always during automated execution

### Description

The checkout form accepts a non-numeric credit card value. A payment form should validate that the card field contains a plausible numeric card value.

### Steps To Reproduce

1. Open https://www.demoblaze.com/
2. Add a product to the cart.
3. Open the cart.
4. Click `Place Order`.
5. Fill name, country, city, month, and year with valid values.
6. Enter `abcd` in the credit card field.
7. Click `Purchase`.

### Expected Result

The application should reject the invalid card value and display a validation message.

### Actual Result

The application displays a purchase confirmation containing an order `Id`.

### Evidence

Automated negative test failed: `tests/test_exploratory_bugs.py::test_checkout_non_numeric_card_should_be_rejected`

### Screenshot Path

`reports/screenshots/BUG-003-checkout-invalid-card.png`

## BUG-004 - Checkout allows purchase with empty cart

**Status:** Confirmed by failing negative test  
**Feature:** Checkout  
**Severity:** High  
**Priority:** Medium  
**Reproducibility:** Always during automated execution

### Description

The cart page allows the user to open the order form and complete a purchase even when no product is in the cart.

### Steps To Reproduce

1. Open https://www.demoblaze.com/
2. Open the cart without adding any product.
3. Click `Place Order`.
4. Fill the order form with valid checkout data.
5. Click `Purchase`.

### Expected Result

The application should prevent checkout because the cart is empty.

### Actual Result

The application displays a purchase confirmation containing an order `Id`, even though no product was added to the cart.

### Evidence

Automated negative test failed: `tests/test_exploratory_bugs.py::test_checkout_empty_cart_should_be_rejected`

### Screenshot Path

`reports/screenshots/BUG-004-empty-cart-checkout.png`
