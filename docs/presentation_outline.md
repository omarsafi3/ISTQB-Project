# Presentation Outline

## Slide 1 - Title

**Tests logiciels assistes par Intelligence Artificielle Generative**  
Application tested: Demoblaze  
Course: Test Logiciel / ISTQB

## Slide 2 - Project Objective

- Apply classic software testing techniques.
- Automate tests with Selenium.
- Use GenAI to improve test design, automation, bug reporting, and result analysis.
- Compare testing before and after GenAI assistance.

## Slide 3 - Tested Application

- Website: https://www.demoblaze.com/
- Type: demo e-commerce web application
- Main features: signup, login/logout, product browsing, cart, checkout, contact form

## Slide 4 - Tools Used

- Python
- Selenium WebDriver
- Selenium Manager
- pytest
- pytest-html
- ChatGPT / Codex as GenAI assistant

## Slide 5 - Test Strategy

- Manual functional test cases
- Automated Selenium regression tests
- Positive tests for normal user journeys
- Negative tests for validation and error handling
- Bug reports with reproducible steps

## Slide 6 - Selenium Project Structure

- `tests/`: pytest test cases
- `pages/`: Page Object Model classes
- `utils/`: driver factory and test data
- `docs/`: manual test cases, bug reports, GenAI usage, results analysis
- `reports/`: HTML reports and screenshots

## Slide 7 - Functional Tests

- Sign up with unique username: passed
- Valid login and logout: passed
- Invalid login: passed
- Product details page: passed
- Add product to cart: passed
- Valid checkout: passed
- Missing required checkout fields: passed
- Contact form with valid data: passed

## Slide 8 - Bugs Found

The exploratory negative tests were written with the expected correct behavior. They failed because Demoblaze accepted invalid inputs.

| Bug ID | Summary | Severity |
|---|---|---|
| BUG-001 | Contact form accepts empty message | Medium |
| BUG-002 | Contact form accepts invalid email | Low |
| BUG-003 | Checkout accepts non-numeric credit card | High |
| BUG-004 | Checkout allows purchase with empty cart | High |

## Slide 9 - Evidence

- Full test report: `reports/full_test_report.html`
- Exploratory bug report: `reports/exploratory_bugs_report.html`
- Screenshots: `reports/screenshots/`
- Bug details: `docs/bug_reports.md`
- Expected interpretation: functional tests pass, negative tests fail and reveal bugs

## Slide 10 - Before GenAI

- Manual test ideas were limited.
- Fewer negative cases were identified.
- No automation structure existed.
- Bug reports were not standardized.

## Slide 11 - After GenAI

- 17 documented manual test cases.
- 13 Selenium automated tests.
- 4 failing negative tests revealing validation bugs.
- Structured Page Object Model project.
- Better bug report and result analysis documentation.

## Slide 12 - GenAI Benefits

- Faster test case generation.
- Better negative scenario coverage.
- Faster Selenium script creation.
- Help with debugging waits and alerts.
- Clearer documentation and summaries.

## Slide 13 - GenAI Limits

- GenAI suggestions must be verified.
- Locators and waits may need correction.
- Public demo websites can be unstable.
- GenAI cannot replace human judgment for bug confirmation.

## Slide 14 - Conclusion

GenAI improved test coverage, automation speed, documentation quality, and bug detection. The final project combines classic functional testing with automated evidence and critical analysis.
