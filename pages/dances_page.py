from selenium.webdriver.common.by import By

from constants.dances_page import DancesPageConst
from pages.base_page import BasePage


class DancesPage(BasePage):
    """Stores methods describes dances page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = DancesPageConst

    def click_dance_style(self, dance_style):
        """Navigate to all dance styles page"""
        self.click(xpath=self.const.DANCE_STYLE_BUTTON_XPATH.format(dance_style=dance_style))

    def verify_dance_style_info_page(self, dance_style):
        """Verify chosen dance style page is displayed"""
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.HEADLINE_NAME_DANCE_XPATH)
        assert self.compare_element_text(xpath=self.const.HEADLINE_NAME_DANCE_XPATH, text=dance_style)

    def click_and_verify_returning_to_dances_page(self):
        """Verify all dance style page is displayed"""
        self.click(xpath=self.const.ALL_DANCES_BUTTON_XPATH)
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.HEADLINE_NAME_DANCE_XPATH)
        assert self.compare_element_text(xpath=self.const.HEADLINE_NAME_DANCE_XPATH,
                                         text=self.const.ALL_DANCE_STYLES_TEXT)
