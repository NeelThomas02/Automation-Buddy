# pages/inventory_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    # locators
    ADD_TO_CART_BTN  = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE       = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK        = (By.CLASS_NAME, "shopping_cart_link")

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
        """Return the number shown on the cart badge (0 if none)."""
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def go_to_cart(self):
        # wait until the cart icon is clickable, then click
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
        # and wait until we’ve actually navigated to /cart.html
        self.wait.until(EC.url_contains("/cart.html"))
