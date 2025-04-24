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

    # 4) Assert we’re back on login page
    #    Sauce Demo shows /index.html or base URL
    assert driver.current_url.rstrip("/").endswith("saucedemo.com")
    # or check login button visible:
    assert driver.find_element(*LoginPage.SUBMIT).is_displayed()
