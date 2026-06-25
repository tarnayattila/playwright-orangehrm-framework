from pages.side_menu import SideMenu
from pages.login_page import LoginPage


def test_navigation_to_pim(page):

    login = LoginPage(page)
    menu = SideMenu(page)

    login.open()
    login.login("Admin", "admin123")

    menu.go_to_pim()

    assert "pim" in page.url.lower()