from config.playwright_config import PlaywrightConfig
from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=PlaywrightConfig.HEADLESS,
            slow_mo=PlaywrightConfig.SLOW_MO
        )

        context = browser.new_context(
            viewport=PlaywrightConfig.VIEWPORT
        )

        page = context.new_page()
        yield page

        context.close()
        browser.close()