from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConst
from pages.base_page import BasePage
from pages.footer import Footer


class StartPage(BasePage):
    """Stores methods describes start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.footer = Footer(self.driver)

    def verify_chosen_language(self, language):
        """Verify the language of interface is as chosen"""

        self.is_element_exists(xpath=self.const.SIGN_IN_BUTTON_XPATH)
        self.wait_until_clickable(by=By.XPATH, xpath=self.const.SIGN_IN_BUTTON_XPATH)
        sleep(1)

        if language == self.footer.const.POLSKI:
            assert self.compare_element_text(xpath=self.const.SIGN_IN_BUTTON_XPATH,
                                             text=self.const.SIGN_IN_BUTTON_TEXT_POLSKI)
        elif language == self.footer.const.ITALIANO:
            assert self.compare_element_text(xpath=self.const.SIGN_IN_BUTTON_XPATH,
                                             text=self.const.SIGN_IN_BUTTON_TEXT_ITALIANO)
        elif language == self.footer.const.ENGLISH:
            assert self.compare_element_text(xpath=self.const.SIGN_IN_BUTTON_XPATH,
                                             text=self.const.SIGN_IN_BUTTON_TEXT_ENGLISH)
        elif language == self.footer.const.ESPANOL:
            assert self.compare_element_text(xpath=self.const.SIGN_IN_BUTTON_XPATH,
                                             text=self.const.SIGN_IN_BUTTON_TEXT_ESPANOL)
        elif language == self.footer.const.DEUTSCH:
            assert self.compare_element_text(xpath=self.const.SIGN_IN_BUTTON_XPATH,
                                             text=self.const.SIGN_IN_BUTTON_TEXT_DEUTSCH)

    def navigate_to_cities_page(self):
        """Navigate to cities page via Find your city button"""
        self.click(xpath=self.const.FIND_CITY_XPATH)

        from pages.cities_page import CitiesPage
        return CitiesPage(self.driver)

    def verify_start_page(self):
        """Verify that Start Page is displayed"""
        assert self.compare_element_text(xpath=self.const.HEADLINE_XPATH, text=self.const.HEADLINE_TEXT, strip=True)

    def navigate_to_community_page(self):
        """Navigate to community page via Find dance partner button"""
        self.click(xpath=self.const.FIND_DANCE_PARTNER_XPATH)

        from pages.community_page import CommunityPage
        return CommunityPage(self.driver)

    def navigate_to_festivals_page(self):
        """Navigate to festivals page via Discover festivals button"""
        self.is_element_visible(xpath=self.const.DISCOVER_FESTIVALS_XPATH)
        self.wait_until_clickable(by=By.XPATH, xpath=self.const.DISCOVER_FESTIVALS_XPATH)
        self.click(xpath=self.const.DISCOVER_FESTIVALS_XPATH)

        from pages.festivals_page import FestivalsPage
        return FestivalsPage(self.driver)
