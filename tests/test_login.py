import pytest
from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")  # Sauce Demo credentials
    # Assert you landed on the inventory page
    assert "inventory.html" in driver.current_url
