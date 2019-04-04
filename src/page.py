from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec

from src.wait import element_present


class Page:
    def __init__(self, base_url, env, browser, open_url=True):
        self.base_url = base_url
        self.env = env
        self.browser = browser

        self.wait = Wait(self.browser, 5)

        self.full_url = f"{self.base_url}{self.path}"
        self.page_is_open = open_url

        if open_url:
            self.get_page(self.full_url)
            self.is_current()
            self.wait_to_load()

    @property
    def path(self):
        raise NotImplementedError()

    @property
    def page_title(self):
        raise NotImplementedError()

    @property
    def page_load_timeout(self):
        raise NotImplementedError()

    @property
    def page_is_loaded(self):
        raise NotImplementedError()

    def get_page(self, url):
        self.browser.set_page_load_timeout(self.page_load_timeout)
        try:
            self.browser.get(url)
        except TimeoutException as err:
            err.msg = (
                "\nTimeout while waiting for page load to complete."
                "\n{page} Load Timeout: {timeout}"
                "\nURL: {url}".format(
                    page=self.__class__.__name__,
                    timeout=self.page_load_timeout,
                    url=url,
                )
            )
            raise

    def is_current(self):
        self.wait.until(
            ec.title_contains(self.page_title),
            message="\nExpected page title: {}."
            "\nActual page title: {}."
            "\nRequested url: {}".format(
                self.page_title, self.browser.title, self.browser.current_url
            ),
        )

    def wait_to_load(self):
        by, value = self.page_is_loaded
        element_present(self.browser, by=by, value=value)

    def __repr__(self):
        msg = "{class_name}('{base_url}', '{env}', '{browser}')"
        return msg.format(
            class_name=self.__class__.__name__,
            base_url=self.base_url,
            env=self.env,
            browser=self.browser.name,
        )

    def __str__(self):
        msg = "{} instance: base_url='{}', browser='{}', url='{}'"
        return msg.format(
            self.__class__.__name__,
            self.base_url,
            self.browser.name,
            self.full_url
        )
