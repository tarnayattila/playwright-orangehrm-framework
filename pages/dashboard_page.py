

class DashboardPage:

    def __init__(self, page):
        self.page = page

        self.header = "h6:has-text('Dashboard')"
        self.user_dropdown = ".oxd-userdropdown-tab"

    def is_loaded(self):
        self.page.locator("h6:has-text('Dashboard')").is_visible()
        return True
    def is_user_menu_visible(self):
        return self.page.locator(self.user_dropdown).is_visible()