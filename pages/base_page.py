from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import config.config as config




class BasePage:
    """
    The BasePage class holds all common functionality for all pages.
    It serves as a wrapper for Selenium actions.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _find_element(self, locator: tuple, timeout: int = config.IMPLICIT_WAIT) -> WebElement:
        """Finds a single web element with an explicit wait."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} not found within {timeout} seconds.")

    def _click(self, locator: tuple, timeout: int = config.IMPLICIT_WAIT):
        """Clicks on a web element."""
        element = self._find_element(locator, timeout)
        element.click()

    def _send_keys(self, locator: tuple, text: str, timeout: int = config.IMPLICIT_WAIT):
        """Sends keys to a web element."""
        element = self._find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator: tuple, timeout: int = config.IMPLICIT_WAIT) -> str:
        """Gets the text of a web element."""
        element = self._find_element(locator, timeout)
        return element.text

    def _get_current_url(self) -> str:
        """Returns the current URL."""
        return self.driver.current_url

    def _wait_for_url_to_contain(self, url_substring: str, timeout: int = config.IMPLICIT_WAIT):
        """Waits for the current URL to contain a specific substring."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(url_substring)
            )
        except TimeoutException:
            raise TimeoutException(
                f"URL did not contain '{url_substring}' within {timeout} seconds. "
                f"Current URL: {self.driver.current_url}"
            )


    def _is_displayed(self, locator: tuple, timeout: int = 1) -> bool:
        """Checks if an element is displayed."""
        try:
            return self._find_element(locator, timeout).is_displayed()
        except TimeoutException:
            return False