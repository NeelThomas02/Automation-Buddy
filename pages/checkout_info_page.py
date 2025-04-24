# pages/checkout_info_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutInfoPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME  = (By.ID, "last-name")
    ZIP_CODE   = (By.ID, "postal-code")
    CONTINUE   = (By.ID, "continue")
    CANCEL     = (By.ID, "cancel")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_info(self, first, last, zip_code):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE).click()
