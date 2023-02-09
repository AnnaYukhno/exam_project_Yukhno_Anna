"""Tests related to community page"""
import pytest

from constants.base import BaseConstants
from constants.dances_page import DancesPageConst


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestCommunityPage:
    """Stores tests for community page functionality"""

    @pytest.mark.parametrize("dance_style", [DancesPageConst.VOGUE_STYLE_TEXT, DancesPageConst.POLE_DANCE_TEXT])
    def test_dance_styles_page(self, community_page, dance_style):
        """
            Steps:
            - Navigate to dance styles page
            - Choose and click dance style
            - Verify dance style info
            - Return to dance style page and verify the result
        """
        # Navigate to dance styles page
        dances_page = community_page.navigate_to_dances_page()

        # Choose and click dance style
        dances_page.click_dance_style(dance_style="".join(dance_style.split()))

        # Verify dance style info
        dances_page.verify_dance_style_info_page(dance_style=dance_style)

        # Return to dance style page and verify the result
        dances_page.click_and_verify_returning_to_dances_page()
