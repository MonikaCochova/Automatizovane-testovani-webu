import pytest
from playwright.sync_api import sync_playwright

#Testování funkčnosti přepnutí do anglické verze
@pytest.fixture(params=["chromium","firefox","webkit"])
def browser(request):
    with sync_playwright() as playwright:
        browser=getattr(playwright, request.param).launch(headless=False, slow_mo=2000)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    page=browser.new_page()
    yield page
    page.close()

def test_english_version(page):
    page.goto("https://www.thajskemasazekiwi.cz/")

    swith_button=page.locator("#header > div > div > div.header-panel > div.header-social > ul > li:nth-child(3) > a")
    swith_button.click()
    page.screenshot(path="screenshot_english_version.png")

    
    button=page.locator("#hp-grid > section:nth-child(1) > div > div > div > a")
    assert button.inner_text()=="BOOK A MASSAGE ONLINE"