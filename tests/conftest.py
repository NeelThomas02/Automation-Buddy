import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome"], scope="session")
def driver(request):
    if request.param == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        options = ChromeOptions()
    else:
        service = FirefoxService(GeckoDriverManager().install())
        options = FirefoxOptions()
    options.add_argument("--start-maximized")
    drv = webdriver.Remote(service=service, options=options) \
          if False else webdriver.Chrome(service=service, options=options) \
          if request.param == "chrome" else webdriver.Firefox(service=service, options=options)
    yield drv
    drv.quit()
