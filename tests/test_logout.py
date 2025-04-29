# tests/test_logout.py

import pytest
from pages.login_page      import LoginPage
from pages.inventory_page  import InventoryPage

def test_logout(driver):
    # 1) Log in
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # 2) Ensure we’re on inventory
    inv = InventoryPage(driver)
    assert "inventory.html" in driver.current_url

    # 3) Log out
    inv.logout()

    # 4) Assert login button is visible on the login page
    # (this guarantees you’re no longer on inventory/checkout)
    assert driver.find_element(*LoginPage.SUBMIT).is_displayed()
