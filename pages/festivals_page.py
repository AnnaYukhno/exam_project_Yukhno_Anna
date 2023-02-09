from selenium.webdriver.common.by import By

from constants.festivals_page import FestivalsPageConst
from pages.base_page import BasePage


class FestivalsPage(BasePage):
    """Stores methods describes festivals page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = FestivalsPageConst

    def click_subscribe_festival(self):
        """Subscribe the chosen festival"""
        self.click(xpath=self.const.SUBSCRIBE_FESTIVAL_XPATH)

    def verify_warning_to_sign_in(self):
        """Verify message is popped up with Sign in button"""
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.MEMBERS_ONLY_XPATH)
        assert self.compare_element_text(xpath=self.const.MEMBERS_ONLY_XPATH, text=self.const.MEMBERS_ONLY_TEXT)
        assert self.is_element_exists(xpath=self.const.SIGN_IN_BUTTON_XPATH)
