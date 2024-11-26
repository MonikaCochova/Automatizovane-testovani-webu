import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

#Testování nákupu dárkového poukazu - zobrazení vybraného voucheru v košíku
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

@pytest.mark.parametrize(
        "voucher_name, selector",
        [
            ("Tradiční thajská masáž", "#online-voucher > div > div > div.col-md-8.col-md-pull-4 > kiwi-shop-productlist > div:nth-child(1) > ul > li:nth-child(1) > div > div.product-info > a"),
            ("Olejová thajská masáž", "#online-voucher > div > div > div.col-md-8.col-md-pull-4 > kiwi-shop-productlist > div:nth-child(1) > ul > li:nth-child(2) > div > div.product-info > a"),
            ("Thajská masáž pro dva (olejová)", "#online-voucher > div > div > div.col-md-8.col-md-pull-4 > kiwi-shop-productlist > div:nth-child(1) > ul > li:nth-child(3) > div > div.product-info > a"),
        ],
        )
def test_voucher(page, voucher_name, selector):
    page.goto("https://www.thajskemasazekiwi.cz/")

    voucher_menu=page.locator("#splide-hp-vouchers-slide01 > div > div > a > span:nth-child(1)")
    voucher_menu.click()

    eshop_button=page.locator("#online-voucher-store > div > div > p.shop-button > a")
    eshop_button.click()

    page.wait_for_load_state("networkidle")

    page.click(f"{selector}")

    page.screenshot(path="screenshot_eshop_voucher.png")

    kosik=page.wait_for_selector("#sidebar > kiwi-shop-cart > div > div > ul > li > div > h4")
    text_v_kosiku = kosik.text_content()
    assert voucher_name in text_v_kosiku

