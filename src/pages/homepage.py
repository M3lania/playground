from types import SimpleNamespace
from selenium.webdriver.common.by import By

from src.page import Page
from src.wait import element_visible

HomePageLocators = SimpleNamespace(
    page_title=(By.CSS_SELECTOR, "head>title"),
    location_input=(By.CSS_SELECTOR, ".form-control"),
    next_button=(By.CSS_SELECTOR, "input.pull-left"),
    location_error=(By.CSS_SELECTOR, "div.alert"),
    geocode_menu_button=(
        By.CSS_SELECTOR,
        "ul.nav.navbar-nav.navbar-right>li:first-child",
    ),
)


class HomePage(Page):

    path = ""
    page_load_timeout = 30
    page_is_loaded = HomePageLocators.page_title

    @property
    def page_title(self):
        return (
            "Geocode.xyz: Geoparse, Geocode and map your geo data to latitude,"
            "longitude and elevation."
        )

    def click_geocode_menu_button(self):
        geocode_menu_button = HomePageLocators.geocode_menu_button
        element_visible(self.browser, *geocode_menu_button)
        self.browser.find_element(*geocode_menu_button).click()

    def fill_in_location(self, value):
        location_input = HomePageLocators.location_input
        element_visible(self.browser, *location_input)
        self.browser.find_element(*location_input).send_keys(value)

    def click_next_button(self):
        next_button = HomePageLocators.next_button
        element_visible(self.browser, *next_button)
        self.browser.find_element(*next_button).click()

    @property
    def location_error(self):
        location_error = HomePageLocators.location_error
        element_visible(self.browser, *location_error)
        return self.browser.find_element(*location_error).text.strip()
