# tests/test_inventory.py

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(driver):
    # 1. Log in
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # 2. On inventory page, cart should start at 0
    inv = InventoryPage(driver)
    assert inv.get_cart_count() == 0

    # 3. Add the first item
    inv.add_first_item_to_cart()

    # 4. Now the badge should show “1”
    assert inv.get_cart_count() == 1

    # 5. Navigate to cart and verify URL
    inv.go_to_cart()
    assert "cart.html" in driver.current_url
