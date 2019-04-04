import pytest
import requests
from faker import Faker
from logzero import logger

from src.demo_robobrowser import SignUp, SignUpError, Locate


@pytest.fixture()
def default_valid_payload():
    faker = Faker()
    email = faker.email()
    password = faker.password()
    return {
        "email": email,
        "conf_email": email,
        "password": password,
        "conf_password": password,
    }


SIGN_UP_PATH = "/new_account"
LOCATE_PATH = ""
HUMAN_PROOF_CHECK = "You must prove you are a human!"


@pytest.mark.env("QA")
def test_successful_registration_using_robobrowser(
    robobrowser, base_url, default_valid_payload
):
    """
    The submission of valid input fields (via RoboBrowser) results to an
    automatic redirection to a new page in which a human proof check is
    performed. (Example of test marked as 'env("QA")'. It will be skipped on
    any environment other than QA.)
    """
    register = SignUp(robobrowser, base_url, path=SIGN_UP_PATH)
    response_text = register.sign_up(**default_valid_payload)
    logger.debug(
        f"Checking that '{HUMAN_PROOF_CHECK}' is displayed on the new page"
    )
    assert HUMAN_PROOF_CHECK in response_text


@pytest.mark.regression
@pytest.mark.parametrize(
    ("email", "conf_email", "password", "conf_password", "message"),
    [
        (
            "test@test.com",
            "2test@test.com",
            "Asdf1234!",
            "Asdf1234!",
            "Email Mismatch! You must Retype your email exactly like you "
            "entered it in the first field.",
        ),
        (
            "test@test.com",
            "test@test.com",
            "Asdf1234!",
            "2Asdf1234!",
            "Password Mismatch! You must Retype your password exactly like you "
            "entered it in the first field.",
        ),
    ],
)
def test_unsuccessful_registration_using_robobrowser(
    robobrowser, base_url, email, conf_email, password, conf_password, message
):
    """
    The incorrect submission of email and password results in an invalid input
    warning. (Example of test marked as 'regression'.)
    """
    register = SignUp(robobrowser, base_url, path=SIGN_UP_PATH)
    try:
        register.sign_up(
            email=email,
            conf_email=conf_email,
            password=password,
            conf_password=conf_password,
        )
    except SignUpError as e:
        logger.debug(f"Checking that '{message}' is displayed on the same page")
        assert message in str(e)


@pytest.mark.incremental
class TestLocalizationFlow:
    """
    Examples of tests which depend on each other. They are used to test the
    localization flow. If the first test fails, the second one will be skipped
    and marked as XFAIL. Useful info can be passed from one test to the other.
    """

    def test_successful_localization_using_robobrowser(
        self, request, robobrowser, base_url
    ):
        """
        When a valid input is used for localization, we get access to a link to
        a new page. E.g. https://geocode.xyz/46.84910,23.63016
        We call this URL as latt_longt_url and we will pass it to the next test.
        """
        localize = Locate(robobrowser, base_url, path=LOCATE_PATH)
        latt_longt_url = localize.latt_longt_url(value="Cluj")
        logger.debug(
            f"Checking that the latitude/longitude URL contains '46.8'"
        )
        assert "46.8" in latt_longt_url
        request.config.cache.set("latitude_url", latt_longt_url)

    def test_localization_api(self, request, robobrowser, env):
        """
        By adding "?json=1" at the end of latt_longt_url we get the same URL as
        the one from the "JSON" button. When we access this page, we get
        latitude-longitude info in JSON format.
        """
        latitude_url = request.config.cache.get("latitude_url", None)
        json_latitude_url = f"{latitude_url}?json=1"
        logger.debug(
            f"Fetching latitude info from API endpoint: {json_latitude_url}"
        )
        response = requests.get(json_latitude_url)
        parsed = response.json()
        logger.debug(f"Extracted JSON response: {parsed}")
        logger.debug(
            f'Checking that "Request Throttled." is part of the JSON response'
        )
        assert "Request Throttled." in parsed["error"]["message"]
