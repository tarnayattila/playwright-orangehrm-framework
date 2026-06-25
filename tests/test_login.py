from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_valid_login(page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open()
    login.login("Admin", "admin123")

    assert dashboard.is_loaded()