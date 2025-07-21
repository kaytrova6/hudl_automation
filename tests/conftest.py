import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import config.config as config


@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture to initialize and quit the WebDriver for each test function.
    The browser type is determined by the 'BROWSER' variable in config.py.
    """
    browser_name = config.BROWSER.lower()
    
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if config.HEADLESS:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")  # Recommended for headless
        _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if config.HEADLESS:
            options.add_argument("--headless")
        _driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        raise ValueError(f"Browser '{config.BROWSER}' is not supported.")

    _driver.implicitly_wait(config.IMPLICIT_WAIT)
    if not config.HEADLESS:
        _driver.maximize_window()

    yield _driver

    _driver.quit()