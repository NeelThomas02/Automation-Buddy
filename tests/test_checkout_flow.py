# tests/test_checkout_flow.py

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_checkout_flow(driver):
    # 1. Login
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # 2. Add an item
    inv = InventoryPage(driver)
    inv.add_first_item_to_cart()
    assert inv.get_cart_count() == 1

    # go straight to the cart page
    cart = CartPage(driver)
    cart.load()
    cart.go_to_checkout()

    # 4. Fill checkout info
    info = CheckoutInfoPage(driver)
    info.fill_info("Jane", "Doe", "12345")

    # 5. Finish overview
    overview = CheckoutOverviewPage(driver)
    overview.finish()

    # 6. Verify completion
    complete = CheckoutCompletePage(driver)
    confirmation = complete.get_confirmation()
    assert "THANK YOU FOR YOUR ORDER" in confirmation.upper()
