from pages.login_page import LoginPage
from utils.faker_utils import generate_employee
from pages.pim_page import PIMPage


def test_add_employee(page):

    login = LoginPage(page)
    pim = PIMPage(page)


    login.open()
    login.login("Admin", "admin123")
    user = generate_employee()

    pim.add_employee(user["first_name"], user["last_name"])

    assert "pim" in page.url.lower()