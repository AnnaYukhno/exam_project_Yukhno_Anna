"""Tests related to festivals page"""
import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestFestivalsPage:
    """Stores tests for festivals page functionality"""

    def test_subscription_to_festival_without_sing_in(self, start_page):
        """
            Steps:
            - Navigate to Festivals page
            - Click Subscribe button
            - Verify warning message is displayed
        """
        # Navigate to Festivals page
        festivals_page = start_page.navigate_to_festivals_page()

        # Click Subscribe button
        festivals_page.click_subscribe_festival()

        # Verify warning message is displayed
        festivals_page.verify_warning_to_sign_in()
