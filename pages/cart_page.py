# pages/cart_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    CART_URL           = "https://www.saucedemo.com/cart.html"
    CHECKOUT_BTN       = (By.ID, "checkout")
    CONTINUE_SHOPPING  = (By.ID, "continue-shopping")
    REMOVE_BTN         = (By.CSS_SELECTOR, ".cart_button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get(self.CART_URL)

    def go_to_checkout(self):
        # double‐check we’re on the cart page
        assert "/cart.html" in self.driver.current_url, f"Not on cart page: {self.driver.current_url}"
        # now click the checkout button
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()

    def remove_all_items(self):
        for btn in self.driver.find_elements(*self.REMOVE_BTN):
            btn.click()
