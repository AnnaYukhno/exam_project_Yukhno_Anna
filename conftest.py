import random

import pytest as pytest

from pages.start_page import StartPage
from pages.utils import create_driver


@pytest.fixture()
def driver(browser):
    """Create selenium driver"""
    driver = create_driver(browser=browser)
    yield driver
    driver.close()


@pytest.fixture()
def start_page(driver):
    """Create start page object"""
    return StartPage(driver)


@pytest.fixture()
def random_city():
    """Chose random city from the list"""
    cities = ['London, United Kingdom', 'Kyiv, Ukraine', 'Paris, France',
              'Los Angeles, United States', 'Munich, Germany']
    return random.choice(cities)


@pytest.fixture()
def community_page(start_page):
    return start_page.navigate_to_community_page()
