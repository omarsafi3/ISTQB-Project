# Manual Test Cases

| ID | Feature | Scenario | Preconditions | Steps | Test Data | Expected Result | Status |
|---|---|---|---|---|---|---|---|
| TC-001 | Sign up | Create a new account with valid data | User is on home page | Click Sign up, enter a unique username and password, click Sign up | Username: generated unique value, Password: Password123 | Success alert is displayed | Passed |
| TC-002 | Sign up | Try to create an account with an existing username | Existing account is known | Click Sign up, enter existing username and password, click Sign up | Username: existing user | Error alert is displayed | Not automated |
| TC-003 | Login / Logout | Login with valid credentials | User has a valid account | Click Log in, enter valid username and password, click Log in | Generated username, Password: Password123 | Welcome message is displayed and Logout link appears | Passed |
| TC-004 | Login / Logout | Login with invalid credentials | User is on home page | Click Log in, enter invalid username/password, click Log in | Invalid username/password | Error alert is displayed | Passed |
| TC-005 | Login / Logout | Logout after successful login | User is logged in | Click Logout | Valid logged-in session | User is logged out and Log in link appears | Passed |
| TC-006 | Product browsing | View product list on home page | User is on home page | Observe displayed products | None | Product cards are visible | Passed |
| TC-007 | Product browsing | Filter products by category | User is on home page | Click Laptops category | Category: Laptops | Products for selected category are displayed | Passed |
| TC-008 | Product browsing | Open product details page | Product list is visible | Click a product name | First visible product | Details page displays product name and price | Passed |
| TC-009 | Cart | Add product to cart | Product details page is open | Click Add to cart, accept alert, open Cart | First visible product | Product appears in cart | Passed |
| TC-010 | Cart | Verify cart content | Product has been added to cart | Open Cart page | Added product | Product name and price are displayed | Passed |
| TC-011 | Checkout | Place order with valid data | Product exists in cart | Click Place Order, fill form, click Purchase | Name, country, city, card, month, year | Confirmation message is displayed | Passed |
| TC-012 | Checkout | Try checkout with missing required fields | Product exists in cart | Click Place Order, leave form empty, click Purchase | Empty checkout form | Required fields alert is displayed | Passed |
| TC-013 | Contact | Send contact message | User is on home page | Click Contact, fill email, name, message, click Send message | Valid email, name, message | Thank-you alert is displayed | Passed |
| TC-014 | Contact | Try sending contact form with empty fields | User is on home page | Click Contact, leave fields empty, click Send message | Empty fields | Application should reject empty contact request | Failed - BUG-001 |
| TC-015 | Contact | Try sending contact form with invalid email | User is on home page | Click Contact, enter invalid email, name, message, click Send message | Email: not-an-email | Application should reject invalid email format | Failed - BUG-002 |
| TC-016 | Checkout | Try checkout with non-numeric credit card | Product exists in cart | Fill checkout form using letters in card field, click Purchase | Card: abcd | Application should reject non-numeric credit card value | Failed - BUG-003 |
| TC-017 | Checkout | Try checkout with empty cart | Cart is empty | Open Cart, click Place Order, fill form, click Purchase | Valid checkout data, no cart item | Application should prevent purchase because cart is empty | Failed - BUG-004 |
