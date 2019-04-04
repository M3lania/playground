from types import SimpleNamespace
from selenium.webdriver.common.by import By

from src.page import Page
from src.wait import element_visible

SignUpPageLocators = SimpleNamespace(
    page_title=(By.CSS_SELECTOR, "head>title"),
    email_first_input=(
        By.CSS_SELECTOR,
        ".alert.alert-info:nth-child(1) .form-control"
    ),
    email_second_input=(
        By.CSS_SELECTOR,
        ".alert.alert-info:nth-child(2) .form-control",
    ),
    password_first_input=(By.CSS_SELECTOR, ".alert-danger:nth-child(3) input"),
    password_second_input=(By.CSS_SELECTOR, ".alert-danger:nth-child(4) input"),
    create_account_button=(By.CSS_SELECTOR, ".btn.btn-large.btn-primary"),
    human_proof_first_paragraph=(By.CSS_SELECTOR, "p.navbar-text"),
)


class SignUpPage(Page):
    path = "/new_account"
    page_load_timeout = 30
    page_is_loaded = SignUpPageLocators.page_title

    @property
    def page_title(self):
        return (
            "Geocode.xyz: Geoparse, Geocode and map your geo data to latitude,"
            "longitude and elevation."
        )

    def fill_in_email_first_input(self, value):
        email_first_input = SignUpPageLocators.email_first_input
        element_visible(self.browser, *email_first_input)
        self.browser.find_element(*email_first_input).send_keys(value)

    def fill_in_email_second_input(self, value):
        email_second_input = SignUpPageLocators.email_second_input
        element_visible(self.browser, *email_second_input)
        self.browser.find_element(*email_second_input).send_keys(value)

    def fill_in_password_first_input(self, value):
        password_first_input = SignUpPageLocators.password_first_input
        element_visible(self.browser, *password_first_input)
        self.browser.find_element(*password_first_input).send_keys(value)

    def fill_in_password_second_input(self, value):
        password_second_input = SignUpPageLocators.password_second_input
        element_visible(self.browser, *password_second_input)
        self.browser.find_element(*password_second_input).send_keys(value)

    def click_create_account_button(self):
        create_account_button = SignUpPageLocators.create_account_button
        element_visible(self.browser, *create_account_button)
        self.browser.find_element(*create_account_button).click()

    @property
    def human_proof_first_paragraph(self):
        first_paragraph = SignUpPageLocators.human_proof_first_paragraph
        element_visible(self.browser, *first_paragraph)
        return self.browser.find_element(*first_paragraph).text.strip()
