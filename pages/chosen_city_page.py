from selenium.webdriver.common.by import By

from constants.chosen_city_page import ChosenCityPageConst
from pages.base_page import BasePage


class ChosenCityPage(BasePage):
    """Stores methods describes actions at page of chosen city"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = ChosenCityPageConst

    def verify_city_name(self, city):
        """Verify chosen city is displayed"""
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.LOCATION_XPATH)
        assert self.compare_element_text(xpath=self.const.LOCATION_XPATH, text=city)

    def navigate_to_start_page(self):
        """Navigate to start page by clicking the button"""
        self.click(xpath=self.const.LOGO_BUTTON_XPATH)

        from pages.start_page import StartPage
        return StartPage(self.driver)
