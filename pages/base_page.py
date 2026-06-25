from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def assert_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()