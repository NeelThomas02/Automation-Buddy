# tests/conftest.py

import sys, os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# allow imports from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="session")
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()

    # 1) Run in Incognito so no Google sign-in/profile leaks in
    options.add_argument("--incognito")

    # 2) Disable all password-manager UIs
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--disable-save-password-bubble")

    # 3) Optional extras
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    # for CI you can uncomment:
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    drv = webdriver.Chrome(service=service, options=options)
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    On test failure, capture a screenshot and embed in the HTML report.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            html_plugin = item.config.pluginmanager.getplugin("html")
            if html_plugin:
                extra = getattr(rep, "extra", [])
                extra.append(html_plugin.extras.image(screenshot_path))
                rep.extra = extra
