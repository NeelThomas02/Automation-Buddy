# pages/checkout_complete_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutCompletePage:
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT   = (By.CLASS_NAME, "complete-text")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_confirmation(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)).text
