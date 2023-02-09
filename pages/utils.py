from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from constants.base import BaseConstants


def create_driver(browser):
    """Creates driver according to provided browser"""
    if browser == BaseConstants.CHROME:
        driver = webdriver.Chrome(executable_path=BaseConstants.CHROME_DRIVER_PATH)
        driver.maximize_window()
    elif browser == BaseConstants.FIREFOX:
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=BaseConstants.FF_DRIVER_PATH, options=options)
    else:
        raise ValueError(f"Unknown browser name: {browser}")
    driver.get(BaseConstants.URL)
    driver.implicitly_wait(1)
    return driver
