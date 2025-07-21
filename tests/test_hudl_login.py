import pytest

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import config.config as config
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_hudl_successful_login(driver):
    """
    Test case for a successful login to Hudl.
    It uses credentials from the config file and validates
    that the user is redirected to the home page.
    """
    # Arrange
    login_page = LoginPage(driver)

    # Act
    login_page.login()

    # Assert
    home_page = HomePage(driver)

    # It's crucial to wait for the page transition to complete before making assertions.
    # We'll wait for the URL to change, which confirms we've landed on the home page.
    home_page._wait_for_url_to_contain("/home", timeout=15)

    # Now that we've synchronized with the page load, we can safely run assertions.
    assert "/home" in home_page._get_current_url(), "Did not redirect to the home page."
    assert home_page.is_user_avatar_displayed(), "User avatar not found on the home page."


@pytest.mark.negative
def test_hudl_unsuccessful_login_with_invalid_password(driver):
    """
    Test case for an unsuccessful login with an invalid password.
    It validates that the correct error message is displayed and
    the user is not redirected.
    """
    # Arrange
    login_page = LoginPage(driver)
    # This is the current error message displayed for an invalid password.
    # The "Need help?" part is a link, but .text should capture it.
    expected_error_message = "Your email or password is incorrect. Try again."

    # Act
    login_page.enter_email(config.HUDL_USER)
    login_page.click_login_button()
    login_page.enter_password("invalid_password_123")
    login_page.click_login_button()

    # Assert
    # This scenario uses the general form error message, not a field-specific one.
    actual_error_message = login_page.get_password_error_message()

    assert actual_error_message.strip() == expected_error_message, "Incorrect error message displayed."
    assert "/home" not in login_page._get_current_url(), "User was redirected unexpectedly."


@pytest.mark.negative
def test_hudl_login_with_invalid_email_format(driver):
    """
    Test case for an unsuccessful login with an invalid email format.
    It validates that the correct field-specific error message is displayed.
    """
    # Arrange
    login_page = LoginPage(driver)
    expected_error_message = "Enter a valid email."

    # Act
    # We only perform the first step of the login to trigger the email validation.
    login_page.enter_email("not-a-valid-email")
    login_page.click_login_button()

    # Assert
    actual_error_message = login_page.get_error_message()
    assert actual_error_message.strip() == expected_error_message, "Incorrect email format error message displayed."
    assert "/home" not in login_page._get_current_url(), "User was redirected unexpectedly."