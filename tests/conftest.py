import pytest

from src.pages.homepage import HomePage
from src.pages.sign_up_page import SignUpPage


@pytest.fixture(scope="function")
def homepage(base_url, env, browser):
    return HomePage(base_url, env, browser)


@pytest.fixture(scope="class")
def homepage_class(base_url, env, class_scoped_browser):
    return HomePage(base_url, env, class_scoped_browser)


@pytest.fixture(scope="function")
def sign_up_page(base_url, env, browser):
    return SignUpPage(base_url, env, browser)
