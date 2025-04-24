# pages/checkout_overview_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOverviewPage:
    FINISH_BTN = (By.ID, "finish")
    CANCEL     = (By.ID, "cancel")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()
