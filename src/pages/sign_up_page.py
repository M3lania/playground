from selenium.webdriver.common.by import By

from src.page import Page
from src.wait import element_visible


class SignUpPageLocators:
    PAGE_TITLE = (By.CSS_SELECTOR, "head>title")
    EMAIL_FIRST_INPUT = (
        By.CSS_SELECTOR,
        ".alert.alert-info:nth-child(1) .form-control",
    )
    EMAIL_SECOND_INPUT = (
        By.CSS_SELECTOR,
        ".alert.alert-info:nth-child(2) .form-control",
    )
    PASSWORD_FIRST_INPUT = (By.CSS_SELECTOR, ".alert-danger:nth-child(3) input")
    PASSWORD_SECOND_INPUT = (By.CSS_SELECTOR, ".alert-danger:nth-child(4) input")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-large.btn-primary")
    HUMAN_PROOF_FIRST_PARAGRAPH = (By.CSS_SELECTOR, "p.navbar-text")


class SignUpPage(Page):

    path = "/new_account"
    page_load_timeout = 30
    page_is_loaded = SignUpPageLocators.PAGE_TITLE

    @property
    def page_title(self):
        return (
            "Geocode.xyz: Geoparse, Geocode and map your geo data to latitude,"
            "longitude and elevation."
        )

    def fill_in_email_first_input(self, value):
        email_first_input = SignUpPageLocators.EMAIL_FIRST_INPUT
        element_visible(self.browser, *email_first_input)
        self.browser.find_element(*email_first_input).send_keys(value)

    def fill_in_email_second_input(self, value):
        email_second_input = SignUpPageLocators.EMAIL_SECOND_INPUT
        element_visible(self.browser, *email_second_input)
        self.browser.find_element(*email_second_input).send_keys(value)

    def fill_in_password_first_input(self, value):
        password_first_input = SignUpPageLocators.PASSWORD_FIRST_INPUT
        element_visible(self.browser, *password_first_input)
        self.browser.find_element(*password_first_input).send_keys(value)

    def fill_in_password_second_input(self, value):
        password_second_input = SignUpPageLocators.PASSWORD_SECOND_INPUT
        element_visible(self.browser, *password_second_input)
        self.browser.find_element(*password_second_input).send_keys(value)

    def click_create_account_button(self):
        create_account_button = SignUpPageLocators.CREATE_ACCOUNT_BUTTON
        element_visible(self.browser, *create_account_button)
        self.browser.find_element(*create_account_button).click()

    @property
    def human_proof_first_paragraph(self):
        first_paragraph = SignUpPageLocators.HUMAN_PROOF_FIRST_PARAGRAPH
        element_visible(self.browser, *first_paragraph)
        return self.browser.find_element(*first_paragraph).text.strip()
