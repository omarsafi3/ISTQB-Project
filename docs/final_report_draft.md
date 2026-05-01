# Final Report Draft

## 1. Introduction

This project was completed for the course **Test Logiciel / ISTQB**. The subject is **Tests logiciels assistes par Intelligence Artificielle Generative**. The goal is to design and execute a software testing process while integrating GenAI tools to improve efficiency and quality.

## 2. Application Under Test

The selected application is **Demoblaze**, available at https://www.demoblaze.com/. Demoblaze is a demo e-commerce website that allows users to browse products, create accounts, log in, add products to the cart, place orders, and send contact messages.

## 3. Functionalities Tested

The project covers 6 functionalities:

- Sign up
- Login / logout
- Product browsing
- Add product to cart
- Checkout / place order
- Contact form

## 4. Test Tools

The testing stack uses:

- Python
- Selenium WebDriver
- Selenium Manager
- pytest
- pytest-html
- ChatGPT / Codex for GenAI assistance

## 5. Classic Testing

Manual test cases were created in `docs/manual_test_cases.md`. Each test case includes an ID, feature, scenario, preconditions, steps, test data, expected result, and status.

The manual test design first focused on normal user journeys. Later, negative scenarios were added to verify validation and error handling.

## 6. Test Automation

The automated tests are written with Selenium and pytest. The project uses the Page Object Model to keep tests readable and maintainable.

Main folders:

- `tests/`: automated test cases
- `pages/`: page classes and locators
- `utils/`: WebDriver setup and test data
- `reports/`: execution reports and screenshots

## 7. Bugs Detected

Exploratory negative tests detected 4 reproducible validation defects. These tests were written with the expected correct behavior, so they failed when Demoblaze accepted invalid input.

| Bug ID | Description | Severity |
|---|---|---|
| BUG-001 | Contact form accepts empty message | Medium |
| BUG-002 | Contact form accepts invalid email format | Low |
| BUG-003 | Checkout accepts non-numeric credit card value | High |
| BUG-004 | Checkout allows purchase with empty cart | High |

Detailed bug reports are available in `docs/bug_reports.md`.

The execution summary is available in `docs/test_execution_summary.md`.

## 8. GenAI Usage

GenAI was used to:

- Generate test case ideas
- Suggest negative test scenarios
- Create Selenium test scripts
- Improve Page Object Model organization
- Improve bug report structure
- Summarize test execution results

All GenAI suggestions were reviewed and verified through real execution.

## 9. Results Before And After GenAI

Before GenAI, the test process was slower and focused mainly on basic manual scenarios. After GenAI, the project included more complete test coverage, automated Selenium tests, structured documentation, and 4 reproduced validation bugs.

GenAI improved speed and organization, but human validation remained necessary.

## 10. Conclusion

The project shows that GenAI can improve software testing by helping generate test cases, automate scripts, and document results. However, GenAI does not replace the tester. The tester must verify all generated tests and confirm each bug using evidence.
