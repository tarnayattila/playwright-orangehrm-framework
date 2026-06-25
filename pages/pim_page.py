class PIMPage:

    def __init__(self, page):
        self.page = page

        self.pim_menu = "a[href*='pim']"
        self.add_btn = "button:has-text('Add')"
        self.first_name = "input[name='firstName']"
        self.last_name = "input[name='lastName']"
        self.save_btn = "button[type='submit']"

    def open(self):
        self.page.wait_for_url("**/dashboard/**")

        pim = self.page.get_by_role("link", name="PIM")
        pim.wait_for(state="visible")
        pim.click()

        self.page.wait_for_url("**/pim/**")

    def add_employee(self, first, last):
        self.open()

        add_btn = self.page.get_by_role("button", name="Add")
        add_btn.wait_for(state="visible")
        add_btn.click()

        self.page.get_by_role("textbox", name="First Name").fill(first)
        self.page.get_by_role("textbox", name="Last Name").fill(last)

        self.page.get_by_role("button", name="Save").click()