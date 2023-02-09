from selenium.webdriver.common.by import By

from constants.cities_page import CitiesPageConst
from pages.base_page import BasePage


class CitiesPage(BasePage):
    """Stores methods describes cities page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = CitiesPageConst

    def search_by_city(self, city):
        """Search city by provided name"""
        self.fill_fields(xpath=self.const.FIND_YOUR_CITY_INPUT_XPATH, value=city)
        result = self.wait_until_displayed(by=By.XPATH, xpath=self.const.SEARCH_RESULT_XPATH)
        result.click()

        from pages.chosen_city_page import ChosenCityPage
        return ChosenCityPage(self.driver)
