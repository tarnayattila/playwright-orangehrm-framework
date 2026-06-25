from pages.login_page import LoginPage

def test_invalid_login(page):

    login = LoginPage(page)

    login.open()
    login.login("wrong", "wrong")

    assert "dashboard" not in page.url