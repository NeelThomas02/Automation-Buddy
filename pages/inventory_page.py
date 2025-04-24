# pages/inventory_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class InventoryPage:
    # locators
    ADD_TO_CART_BTN  = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE       = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK        = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BTN    = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_first_item_to_cart(self):
        """Click the first Add to Cart button on the inventory list."""
        btn = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BTN)
        )
        btn.click()

    def get_cart_count(self) -> int:
        """
        Wait up to 10s for the cart badge to appear, then return its count.
        Returns 0 if no badge shows up in time.
        """
        try:
            # wait for the badge to be visible
            badge_elem = self.wait.until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            return int(badge_elem.text)
        except TimeoutException:
            return 0

    def go_to_cart(self):
        # wait until the cart icon is clickable, then click
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
        # and wait until we’ve actually navigated to /cart.html
        self.wait.until(EC.url_contains("/cart.html"))

    def logout(self):
        """Open the side menu and click “Logout”."""
        # 1) open menu
        self.wait.until(EC.element_to_be_clickable(self.MENU_BTN)).click()
        # 2) click logout
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()
