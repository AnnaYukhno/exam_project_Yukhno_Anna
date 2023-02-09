from constants.footer import FooterConsts
from pages.base_page import BasePage


class Footer(BasePage):
    """Stores methods describes footer actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = FooterConsts

    def choose_and_change_language(self, language):
        """Change interface language via footer button"""

        if language == self.const.ENGLISH:
            self.click(self.const.LANGUAGE_OPTION_ENGLISH_XPATH)
        elif language == self.const.ESPANOL:
            self.click(self.const.LANGUAGE_OPTION_ESPANOL_XPATH)
        elif language == self.const.DEUTSCH:
            self.click(self.const.LANGUAGE_OPTION_DEUTSCH_XPATH)
        elif language == self.const.ITALIANO:
            self.click(self.const.LANGUAGE_OPTION_ITALIANO_XPATH)
        elif language == self.const.POLSKI:
            self.click(self.const.LANGUAGE_OPTION_POLSKI_XPATH)

        from pages.start_page import StartPage
        return StartPage(self.driver)
