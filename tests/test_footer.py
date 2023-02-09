"""Tests related to footer"""
import pytest

from constants.base import BaseConstants
from constants.footer import FooterConsts


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestFooter:
    """Stores tests for footer functionality"""

    @pytest.mark.parametrize("language", [FooterConsts.POLSKI, FooterConsts.ITALIANO, FooterConsts.ENGLISH,
                                          FooterConsts.DEUTSCH, FooterConsts.ESPANOL])
    def test_interface_language(self, start_page, language):
        """
            Steps:
            - Change language to provided one
            - Verify the chosen language
        """
        # Change language to provided one
        start_page.footer.choose_and_change_language(language=language)

        # Verify the chosen language
        start_page.verify_chosen_language(language=language)
