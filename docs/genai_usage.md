# GenAI Usage

## Tools Used

GenAI was used through ChatGPT / Codex during the project preparation and implementation.

## Generating Test Cases

GenAI helped propose functional test cases for the Demoblaze website. The selected features were:

- Sign up
- Login and logout
- Product browsing
- Add product to cart
- Checkout / place order
- Contact form

The generated ideas were reviewed and organized in `docs/manual_test_cases.md`.

## Suggesting Negative Test Cases

GenAI helped identify negative and exploratory scenarios that were not obvious in the first manual approach:

- Invalid login
- Checkout with missing required fields
- Contact form with empty fields
- Contact form with invalid email format
- Checkout with a non-numeric credit card value
- Checkout with an empty cart

These negative tests helped detect 4 confirmed validation defects.

## Helping Write Selenium Scripts

GenAI helped create a Selenium automation project using:

- Python
- pytest
- Selenium WebDriver
- Selenium Manager
- Explicit waits
- Page Object Model

The project was organized into `pages/`, `tests/`, `utils/`, `docs/`, and `reports/`.

## Improving Bug Reports

GenAI helped create a bug report template with:

- Bug ID
- Title
- Description
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Priority
- Screenshot path
- Reproducibility

The confirmed bugs are documented in `docs/bug_reports.md`. The negative tests are written to fail when the application does not respect the expected validation behavior.

## Summarizing Test Results

GenAI helped summarize the test execution results and prepare the analysis before and after using GenAI. The main result is that functional tests passed, while exploratory negative tests failed and revealed validation defects.

## Human Validation

All GenAI suggestions were verified by executing Selenium tests. This is important because GenAI can generate incorrect assumptions. The final bug list only includes behavior reproduced with automated tests.

## Example Prompts Used

- "Create Selenium pytest tests for Demoblaze using Page Object Model."
- "Suggest negative test cases for an e-commerce checkout and contact form."
- "Help document bug reports without inventing fake bugs."
- "Analyze test results before and after using GenAI."
