import pytest
from playwright.sync_api import sync_playwright

# Test webových stránek společnosti Thajské masáže Kiwi a jejich obchodně nejdůležitějšího prvku na stránce - online rezervace
# Testování funkčnosti dropdown menu u výběru délky masáží
# Test proběhne na Chromium, Firefox a Webkit
@pytest.fixture(params=["chromium","firefox","webkit"])
def browser(request):
    with sync_playwright() as playwright:
        browser=getattr(playwright, request.param).launch(headless=False, slow_mo=1000)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    page=browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    page.close()

def test_rezervace_60min(page):
    page.goto("https://www.thajskemasazekiwi.cz/")
    button=page.locator("#hp-grid > section:nth-child(1) > div > div > div > a")
    button.click()

    page.wait_for_load_state("networkidle")

    massage_container_1=page.locator("#online-voucher > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > div > div")
    dropdown=page.locator("#online-voucher > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > div > div > div.col-sm-10 > div > div.col-sm-5.col-sm-offset-1 > div.default-form.massage-length-select > ng-select > div > div.ui-select-match > span")
    dropdown.wait_for(timeout=5000) 
    dropdown.click()

#Výběr z dropdown menu [0]
    option_60_minutes=page.locator(".ui-select-choices-row").filter(has_text="60 min")
    option_60_minutes.click()

    selected_value=dropdown.locator(".ui-select-match-text").text_content()
    
    confirm_button=page.locator("#online-voucher > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > div > div > div.col-sm-10 > div > div.col-sm-5.col-sm-offset-1 > div.product-info > a")
    confirm_button.click()
    reservation=page.locator("#page-content > div > section:nth-child(1) > div > div > div > div > div.col-sm-6 > div > div > div").text_content()
    page.screenshot(path="screenshot_after_select_60.png")
    assert "60" in selected_value
    assert "60" in reservation

def test_rezervace_90min(page):
    page.goto("https://www.thajskemasazekiwi.cz/")
    button=page.locator("#hp-grid > section:nth-child(1) > div > div > div > a")
    button.click()

    page.wait_for_load_state("networkidle")

    massage_container_1=page.locator("#online-voucher > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > div > div")
    dropdown=page.locator("#online-voucher > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > div > div > div.col-sm-10 > div > div.col-sm-5.col-sm-offset-1 > div.default-form.massage-length-select > ng-select > div > div.ui-select-match > span")
    dropdown.wait_for(timeout=5000) 
    dropdown.click()

#Výběr z dropdown menu [1]
    option_90_minutes=page.locator(".ui-select-choices-row").filter(has_text="90 min")
    option_90_minutes.click()

    selected_value=dropdown.locator(".ui-select-match-text").text_content()
    
    confirm_button=page.locator("#online-voucher > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > div > div > div.col-sm-10 > div > div.col-sm-5.col-sm-offset-1 > div.product-info > a")
    confirm_button.click()
    reservation=page.locator("#page-content > div > section:nth-child(1) > div > div > div > div > div.col-sm-6 > div > div > div").text_content()
    page.screenshot(path="screenshot_after_select_90.png")
    assert "90" in selected_value
    assert "90" in reservation

def test_rezervace_120min(page):
    page.goto("https://www.thajskemasazekiwi.cz/")
    button=page.locator("#hp-grid > section:nth-child(1) > div > div > div > a")
    button.click()

    page.wait_for_load_state("networkidle")

    massage_container_1=page.locator("#online-voucher > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > div > div")
    dropdown=page.locator("#online-voucher > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > div > div > div.col-sm-10 > div > div.col-sm-5.col-sm-offset-1 > div.default-form.massage-length-select > ng-select > div > div.ui-select-match > span")
    dropdown.wait_for(timeout=5000) 
    dropdown.click()

#Výběr z dropdown menu [2]
    option_120_minutes=page.locator(".ui-select-choices-row").filter(has_text="120 min")
    option_120_minutes.click()

    selected_value=dropdown.locator(".ui-select-match-text").text_content()
    
    confirm_button=page.locator("#online-voucher > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > div > div > div.col-sm-10 > div > div.col-sm-5.col-sm-offset-1 > div.product-info > a")
    confirm_button.click()
    
    reservation=page.locator("#page-content > div > section:nth-child(1) > div > div > div > div > div.col-sm-6 > div > div > div").text_content()
    page.screenshot(path="screenshot_after_select_120.png")
    assert "120" in selected_value
    assert "120" in reservation