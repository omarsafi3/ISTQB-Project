# Results Analysis

## Before GenAI

Before using GenAI, the testing activity was mainly manual and focused on obvious user journeys:

- Number of initial manual test ideas: about 8 to 10
- Main focus: sign up, login, product browsing, cart, checkout, and contact form
- Main difficulty: identifying negative test cases and organizing them clearly
- Weak points: fewer edge cases, no automated regression suite, and no structured bug report format

The first approach was useful for understanding the website, but it was slower and less systematic.

## After GenAI

After using GenAI, the project became more structured and complete:

- Number of documented manual test cases: 17
- Number of automated Selenium tests: 13
- Number of exploratory bug checks: 4
- Number of confirmed bugs / validation defects: 4
- Documentation added: README, manual test cases, bug reports, GenAI usage, results analysis
- Functional regression result: 9 passed, 0 failed
- Exploratory negative result: 4 failed, revealing 4 bugs

GenAI helped transform manual scenarios into Selenium tests using Python, pytest, explicit waits, and the Page Object Model.

## Quality Of Test Cases

The quality of the test cases improved after GenAI assistance:

- Test cases became clearer, with preconditions, steps, test data, expected result, and status.
- Positive and negative scenarios were both covered.
- The tests covered the main functionalities required by the project: sign up, login/logout, product browsing, cart, checkout, and contact.
- The automated tests became reusable because the project uses Page Object Model classes.

The most important improvement was the addition of negative validation tests, which detected real defects.

## Number And Relevance Of Detected Bugs

The normal functional tests passed, but exploratory negative tests failed because the application accepted invalid data. These failures reveal 4 validation defects.

| ID | Bug / Observation | Feature | Severity | Status | Evidence |
|---|---|---|---|---|---|
| BUG-001 | Contact form accepts empty message | Contact | Medium | Confirmed by failing negative test | `tests/test_exploratory_bugs.py`, `reports/exploratory_bugs_report.html` |
| BUG-002 | Contact form accepts invalid email format | Contact | Low | Confirmed by failing negative test | `tests/test_exploratory_bugs.py`, `reports/exploratory_bugs_report.html` |
| BUG-003 | Checkout accepts non-numeric credit card value | Checkout | High | Confirmed by failing negative test | `tests/test_exploratory_bugs.py`, `reports/exploratory_bugs_report.html` |
| BUG-004 | Checkout allows purchase with empty cart | Checkout | High | Confirmed by failing negative test | `tests/test_exploratory_bugs.py`, `reports/exploratory_bugs_report.html` |

These bugs are relevant because they concern input validation and checkout behavior, which are important for an e-commerce application.

## Time / Effort Gain

GenAI reduced effort in several areas:

- Test design: faster generation of functional and negative test ideas.
- Automation: faster creation of Selenium scripts and Page Object classes.
- Documentation: faster preparation of README, bug report templates, and analysis sections.
- Debugging: assistance in fixing Selenium timing issues, especially JavaScript alert handling.

Manual verification was still necessary because GenAI suggestions must be validated against the real application behavior.

## Limits Of GenAI

The project also showed limits of GenAI:

- GenAI can suggest a test that looks logical but does not match the actual website.
- Some generated Selenium locators or waits may need adjustment after execution.
- Automated tests depend on the availability and stability of the public Demoblaze website.
- GenAI cannot confirm a bug by itself; the bug must be reproduced manually or with automation.

## Conclusion

GenAI improved the project by increasing test coverage, adding negative scenarios, helping create Selenium automation, and improving documentation quality. The final result is stronger than manual testing alone because it includes reproducible automated evidence and a clearer analysis of detected defects.
