from constants.community_page import CommunityPageConst
from pages.base_page import BasePage


class CommunityPage(BasePage):
    """Stores methods describes community page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = CommunityPageConst

    def navigate_to_dances_page(self):
        """Navigate to dances page via Dances button"""
        self.click(xpath=self.const.DANCES_BUTTON_XPATH)

        from pages.dances_page import DancesPage
        return DancesPage(self.driver)
