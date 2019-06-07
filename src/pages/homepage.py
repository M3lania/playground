from selenium.webdriver.common.by import By

from src.page import Page
from src.wait import element_visible


class HomePageLocators:
    PAGE_TITLE = (By.CSS_SELECTOR, "head>title")
    LOCATION_INPUT = (By.CSS_SELECTOR, ".form-control")
    NEXT_BUTTON = (By.CSS_SELECTOR, "input.pull-left")
    LOCATION_ERROR = (By.CSS_SELECTOR, "div.alert")
    GEOCODE_MENU_BUTTON = (
        By.CSS_SELECTOR,
        "ul.nav.navbar-nav.navbar-right>li:first-child",
    )


class HomePage(Page):

    path = ""
    page_load_timeout = 30
    page_is_loaded = HomePageLocators.PAGE_TITLE

    @property
    def page_title(self):
        return (
            "Geocode.xyz: Geoparse, Geocode and map your geo data to latitude,"
            "longitude and elevation."
        )

    @property
    def location_error(self):
        location_error = HomePageLocators.LOCATION_ERROR
        element_visible(self.browser, *location_error)
        return self.browser.find_element(*location_error).text.strip()

    def click_geocode_menu_button(self):
        geocode_menu_button = HomePageLocators.GEOCODE_MENU_BUTTON
        element_visible(self.browser, *geocode_menu_button)
        self.browser.find_element(*geocode_menu_button).click()

    def fill_in_location(self, value):
        location_input = HomePageLocators.LOCATION_INPUT
        element_visible(self.browser, *location_input)
        self.browser.find_element(*location_input).send_keys(value)

    def click_next_button(self):
        next_button = HomePageLocators.NEXT_BUTTON
        element_visible(self.browser, *next_button)
        self.browser.find_element(*next_button).click()
