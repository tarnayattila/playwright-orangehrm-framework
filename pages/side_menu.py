
class SideMenu:

    def __init__(self, page):
        self.page = page
        self.pim = "a[href*='pim']"
        self.user_dropdown = ".oxd-userdropdown-tab"
        self.logout_btn = "a:has-text('Logout')"

    def open_user_dropdown(self):
        self.page.click(self.user_dropdown)

    def logout(self):
        self.page.locator(self.user_dropdown).click()

        logout = self.page.get_by_role("menuitem", name="Logout")
        logout.click()

    def go_to_pim(self):
        self.page.click(self.pim)

