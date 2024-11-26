import pytest
from playwright.sync_api import sync_playwright

#Testování kontaktního formuláře - nevalidní vstupy, chybová hláška
@pytest.fixture(params=["chromium","firefox","webkit"])
def browser(request):
    with sync_playwright() as playwright:
        browser=getattr(playwright, request.param).launch(headless=False, slow_mo=5000)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    page=browser.new_page()
    yield page
    page.close()

@pytest.mark.parametrize("name, email, text, error",
    [
        (" ", " ", " ", True),
        ("Monika", "monika.cochova", "text", True),
        ("Monika", "monika.cochova@?/.cz", "text", True),
        ],
)
def test_contact_form(page, name, email, text, error):
    name_field=page.locator("#contact-name")
    email_field=page.locator("#contact-email")
    text_field=page.locator("#contact-message")
    submit_button=page.locator("#contact-form > div > div:nth-child(2) > div:nth-child(2) > button")
    error_location=page.locator("#contact-form > p.c-alert-message.m-warning.m-validation-error")

    page.goto("https://www.thajskemasazekiwi.cz/kontakt-praha")
    page.wait_for_load_state("networkidle")

    name_field.fill(name)
    email_field.fill(email)
    text_field.fill(text)
    submit_button.click()

    page.screenshot(path="contact_form_error.png")

    assert error_location.is_visible()==True