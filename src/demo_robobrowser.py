from logzero import logger


class Base:
    def __init__(self, robobrowser, base_url, path):
        self.robobrowser = robobrowser
        self.base_url = base_url
        self.path = path

    @property
    def full_url(self):
        return f"{self.base_url}{self.path}"

    def open_page(self):
        logger.debug(f"Opening {self.full_url}")
        self.robobrowser.open(self.full_url)
        response = self.robobrowser.response
        response.raise_for_status()


class SignUp(Base):
    def sign_up(self, email, conf_email, password, conf_password):
        self.open_page()

        form = self.robobrowser.get_form()
        form["email"] = email
        form["conf_email"] = conf_email
        form["pass"] = password
        form["pass_conf"] = conf_password
        logger.debug(f"Submitting form {form}")
        self.robobrowser.submit_form(form)

        errors = self.robobrowser.select("td.text")
        if errors:
            raise Exception(errors[0].text)
        return self.robobrowser.response.text


class Locate(Base):
    def locate(self, value):
        self.open_page()

        form = self.robobrowser.get_form()
        form["locate"] = value
        logger.debug(f"Submitting form {form}")
        self.robobrowser.submit_form(form)

        errors = self.robobrowser.select("div.alert.alert-danger")
        if errors:
            raise Exception(errors[0].text)
        return self.robobrowser

    def latt_longt_url(self, value):
        latt_longt_page = self.locate(value)
        latt_longt = latt_longt_page.select("p#bg-text >small>a")
        latt_longt_url = latt_longt[0].attrs["href"]
        logger.debug(f"Extracted latitude/longitude URL: {latt_longt_url}")
        return latt_longt_url
