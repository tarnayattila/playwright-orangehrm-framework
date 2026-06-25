from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.side_menu import SideMenu


def test_logout(page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    menu = SideMenu(page)

    login.open()
    login.login("Admin", "admin123")

    assert dashboard.is_loaded()

    menu.open_user_dropdown()
    menu.logout()

    assert "login" in page.url.lower()