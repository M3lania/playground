import pytest
from selenium import webdriver
from robobrowser import RoboBrowser

ENV = {"PROD": "https://geocode.xyz", "QA": "https://qa.geocode.xyz"}


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        dest="env",
        default="PROD",
        choices=("PROD", "QA"),
        help="The environment for the application under test.",
    )

    parser.addoption(
        "--browser",
        action="store",
        dest="browser",
        default="chrome",
        choices=("firefox", "chrome"),
        help="Select your desired browser.",
    )


def pytest_configure(config):
    """
    Custom marker - via https://docs.pytest.org/en/latest/example/markers.html
    This runs after command line options have been parsed.
    """
    # Register an additional marker.
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )


@pytest.fixture(scope="session")
def env(request):
    e = request.config.getoption("--env")
    return e.upper()


@pytest.fixture(scope="function")
def browser(request):
    browser = request.config.getoption("browser").lower()
    if browser == "chrome":
        browser = webdriver.Chrome()
    elif browser == "firefox":
        browser = webdriver.Firefox()
    yield browser
    browser.close()


@pytest.fixture(scope="class")
def class_scoped_browser(request):
    browser = request.config.getoption("browser").lower()
    if browser == "chrome":
        browser = webdriver.Chrome()
    elif browser == "firefox":
        browser = webdriver.Firefox()
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def base_url(env):
    return ENV[env]


@pytest.fixture(scope="class")
def robobrowser():
    """
    RoboBrowser is a Pythonic library for browsing the web without a standalone
    web browser. It can fetch a page, click on links/buttons, fill out and
    submit forms >>  https://robobrowser.readthedocs.io/en/latest/readme.html
    """
    yield RoboBrowser(history=True, parser="html.parser")


"""
Incremental Testing: If one test fails, it makes no sense to execute further (dependent) 
tests, as they are all expected to fail. Below, we introduce an 'incremental' marker 
which is to be used on classes. >> https://docs.pytest.org/en/latest/example/simple.html
"""


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    """ This runs before every test with pytest. """
    envnames = [mark.args[0] for mark in item.iter_markers(name="env")]
    if envnames:
        if item.config.getoption("env") not in envnames:
            pytest.skip(f"test requires env in {envnames}")

    print()
    item_length = len(item._nodeid)
    print("-" * item_length)

    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail(f"previous test failed {previousfailed.name}")
