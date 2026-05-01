# Demoblaze Selenium Testing Project

## Objective

This university project was created for the course **Test Logiciel / ISTQB**.
The objective is to test a web application using classic functional testing and Selenium automation, then compare the work before and after assistance from Generative AI.

## Tested Website

- Website: https://www.demoblaze.com/
- Type: Demo e-commerce web application

## Functionalities Tested

1. Sign up
2. Login and logout
3. Product browsing
4. Add product to cart
5. Checkout / place order
6. Contact form

## Tools Used

- Python
- Selenium WebDriver
- Selenium Manager
- pytest
- pytest-html
- Page Object Model

## Project Structure

```text
demoblaze-selenium-testing/
|-- README.md
|-- requirements.txt
|-- pytest.ini
|-- tests/
|-- pages/
|-- utils/
|-- docs/
`-- reports/
    `-- screenshots/
```

## Installation

1. Open a terminal in this folder:

```bash
cd demoblaze-selenium-testing
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

Chrome must be installed on the machine. Selenium Manager will handle the browser driver automatically.

## How To Run Tests

Run all tests:

```bash
pytest
```

Note: the exploratory negative tests are designed to fail when they reveal real bugs. For a clean passing regression report, run only the functional tests.

Run one test file:

```bash
pytest tests/test_login.py
```

Run smoke tests:

```bash
pytest -m smoke
```

Run negative tests:

```bash
pytest -m negative
```

Run exploratory bug checks:

```bash
pytest tests/test_exploratory_bugs.py
```

Generate an HTML evidence report for exploratory bugs:

```bash
pytest tests/test_exploratory_bugs.py --html=reports/exploratory_bugs_report.html --self-contained-html
```

Generate a clean passing report for functional tests:

```bash
pytest tests/test_signup.py tests/test_login.py tests/test_products.py tests/test_cart.py tests/test_checkout.py tests/test_contact.py --html=reports/functional_tests_report.html --self-contained-html
```

## Presentation Mode

The framework includes a small delay between Selenium actions so the browser movement can be observed during the presentation.

Default delay:

```text
PRESENTATION_DELAY=0.7 seconds
```

To make the demo slower:

```powershell
$env:PRESENTATION_DELAY='1.5'
pytest tests/test_signup.py tests/test_login.py tests/test_products.py tests/test_cart.py tests/test_checkout.py tests/test_contact.py
```

To run faster again:

```powershell
$env:PRESENTATION_DELAY='0'
pytest
```

## How To Generate Reports

Generate a full HTML report:

```bash
pytest --html=reports/full_test_report.html --self-contained-html
```

Screenshots are automatically saved in `reports/screenshots/` when a test fails.

## Team / Project Deliverables

- Manual functional test cases: `docs/manual_test_cases.md`
- Bug report template: `docs/bug_report_template.md`
- Verified bugs and observations: `docs/bug_reports.md`
- GenAI usage documentation: `docs/genai_usage.md`
- Results analysis: `docs/results_analysis.md`
- Test execution summary: `docs/test_execution_summary.md`
- Final report draft: `docs/final_report_draft.md`
- Presentation outline: `docs/presentation_outline.md`
- Selenium automated tests: `tests/`
- Page Object Model classes: `pages/`
- Test execution reports: `reports/`

## Notes For Students

- Some tests interact with a public demo website, so results may vary depending on site availability and data state.
- The signup test generates a unique username to avoid duplicate user errors.
- Do not invent bugs in the final report. Use the bug template only for verified defects or clearly mark items as **Potential bug / observation** until confirmed.
- Use `docs/bug_reports.md` to document suspicious behavior found during exploratory testing.

