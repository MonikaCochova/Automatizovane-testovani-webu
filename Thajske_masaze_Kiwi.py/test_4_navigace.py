import pytest
from playwright.sync_api import sync_playwright

#Testování navigace z hlavního panelu na správnou URL
@pytest.fixture(params=["chromium", "firefox", "webkit"])
def browser(request):
    with sync_playwright() as playwright:
        browser=getattr(playwright, request.param).launch(headless=False,slow_mo=500)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    page=browser.new_page()
    yield page
    page.close()

@pytest.mark.parametrize(
    "selector_menu, expected_url", 
    [("#header > div > div > div.header-navigation > nav > ul > li.m-active > span > a", "https://www.thajskemasazekiwi.cz/"), #Úvodní stránka
     ("#header > div > div > div.header-navigation > nav > ul > li:nth-child(3) > span > a", "https://www.thajskemasazekiwi.cz/rezervace/"), #Online rezervace
     ("#header > div > div > div.header-navigation > nav > ul > li:nth-child(4) > span > a", "https://www.thajskemasazekiwi.cz/masaze-a-ceny"), #Masáže a ceny
     ("#header > div > div > div.header-navigation > nav > ul > li:nth-child(5) > span > a", "https://www.thajskemasazekiwi.cz/premium"), #Kiwi premium
     ("#header > div > div > div.header-navigation > nav > ul > li:nth-child(6) > span > a", "https://www.thajskemasazekiwi.cz/darkovy-poukaz"), #Dárkový poukaz
     ("#header > div > div > div.header-navigation > nav > ul > li:nth-child(7) > span > a", "https://www.thajskemasazekiwi.cz/doporuceni/"), #Doporučit přítele
     ("#header > div > div > div.header-navigation > nav > ul > li:nth-child(8) > span > a", "https://www.thajskemasazekiwi.cz/maserky"), #Masérky a recepční
     ("#header > div > div > div.header-navigation > nav > ul > li:nth-child(9) > span > a", "https://www.thajskemasazekiwi.cz/galerie"), #Fotogalerie
     ("#header > div > div > div.header-navigation > nav > ul > li:nth-child(10) > span > a", "https://www.thajskemasazekiwi.cz/platebni-poukazky"), #Zaměstnanecké benefity
     ("#header > div > div > div.header-navigation > nav > ul > li:nth-child(11) > span > a", "https://www.thajskemasazekiwi.cz/caste-dotazy"), #Další informace
     ("#header > div > div > div.header-navigation > nav > ul > li:nth-child(12) > span > a", "https://www.thajskemasazekiwi.cz/kontakt-praha"), #Kontakt
     ]
)
def test_navigace(page,selector_menu,expected_url):
    page.goto("https://www.thajskemasazekiwi.cz/")
    page.get_by_role(selector_menu)
    assert page.url==expected_url