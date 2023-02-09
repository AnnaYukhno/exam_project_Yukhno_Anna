"""Tests related to cities page"""
import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestCitiesPage:
    """Stores tests for cities page functionality"""

    def test_searching_by_city(self, start_page, random_city):
        """
            Steps:
            - Navigate to Cities page
            - Search by provided city
            - Verify chosen city is displayed
        """
        # Navigate to Cities page
        cities_page = start_page.navigate_to_cities_page()

        # Search by provided city
        chosen_city_page = cities_page.search_by_city(city=random_city)

        # Verify chosen city is displayed
        chosen_city_page.verify_city_name(city=random_city)

    @pytest.fixture()
    def chosen_city_page(self, start_page, random_city):
        cities_page = start_page.navigate_to_cities_page()
        chosen_city_page = cities_page.search_by_city(city=random_city)
        return chosen_city_page

    def test_return_to_start_page(self, chosen_city_page):
        """
            Steps:
            - Navigate to Start page
            - Verify the result
        """
        # Navigate to Start page
        start_page = chosen_city_page.navigate_to_start_page()

        # Verify the result
        start_page.verify_start_page()
