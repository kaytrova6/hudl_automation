from selenium.webdriver.common.by import By

from .base_page import BasePage


class HomePage(BasePage):
    """Page Object for the Hudl Home page after login."""

    # Locators
    
    _USER_AVATAR = (By.CSS_SELECTOR, ".hui-globaluseritem__avatar")

    def __init__(self, driver):
        super().__init__(driver)

    def is_user_avatar_displayed(self) -> bool:
        """
        Verifies if the user avatar is displayed on the home page.
        We use a longer timeout here as the element may take time to appear after login.
        """
        # The default timeout for _is_displayed is low (1s), so we override it.
        return self._is_displayed(self._USER_AVATAR, timeout=10)