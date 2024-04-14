import pytest

from autotests.config.playwright import Playwright
from playwright.sync_api import Page, sync_playwright


@pytest.fixture()
def page() -> Page:
    playwright = sync_playwright().start()
    if Playwright.BROWSER == 'firefox':
        browser = playwright.firefox.launch()
        context = browser.new_context()
        page_data = context.new_page()
    elif Playwright.BROWSER == 'chrome':
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page_data = context.new_page()
    else:
        browser = playwright.webkit.launch()
        context = browser.new_context()
        page_data = context.new_page()
    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()