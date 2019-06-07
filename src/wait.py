from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def element_present(browser, by, value, timeout=10):
    message = (
        f'\nWaited {timeout} seconds before timing out.'
        f'\nExpected element to be present: {value}'
        f'\nCurrent url: {browser.current_url}'
    )
    WebDriverWait(browser, timeout).until(
        ec.presence_of_element_located((by, value)), message=message
    )


def element_visible(browser, by, value, timeout=10):
    message = (
        f'\nWaited {timeout} seconds before timing out.'
        f'\nExpected element to be visible: {value}'
        f'\nCurrent url: {browser.current_url}'
    )
    WebDriverWait(browser, timeout).until(
        ec.visibility_of_element_located((by, value)), message=message
    )
