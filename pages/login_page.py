from selenium.webdriver.common.by import By

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import config.config as config
from .base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the Hudl login page."""

    # Locators
    _EMAIL_INPUT = (By.ID, "username")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    _ERROR_MESSAGE = (By.ID, "error-element-username")
    _PASSWORD_ERROR_MESSAGE = (By.ID, "error-element-password")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(config.BASE_URL)

    def enter_email(self, email: str):
        """Enters the email into the email field."""
        self._send_keys(self._EMAIL_INPUT, email)

    def enter_password(self, password: str):
        """Enters the password into the password field."""
        self._send_keys(self._PASSWORD_INPUT, password)

    def click_login_button(self):
        """Clicks the login button."""
        self._click(self._LOGIN_BUTTON)

    def login(self):
        """Performs a full, successful login action using credentials from the config."""
        self.enter_email(config.HUDL_USER)
        self.click_login_button()
        self.enter_password(config.HUDL_PASS)
        self.click_login_button()

    def get_error_message(self) -> str:
        """Returns the text of the error message."""
        return self._get_text(self._ERROR_MESSAGE)

    def get_password_error_message(self) -> str:
        """Returns the text of the password-specific error message."""
        return self._get_text(self._PASSWORD_ERROR_MESSAGE)