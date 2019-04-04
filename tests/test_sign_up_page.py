from faker import Faker

FIRST_PARAGRAPH = "Hi {}! You must prove you are a human!"


class TestSignUpPageElements:
    pass


class TestSignUpPageHappyFlow:
    def test_sign_up_with_valid_data(self, sign_up_page):
        """
        A correct submission of email and password leads to a human proof check.
        """
        faker = Faker()
        email = faker.email()
        password = faker.password()
        sign_up_page.fill_in_email_first_input(email)
        sign_up_page.fill_in_email_second_input(email)
        sign_up_page.fill_in_password_first_input(password)
        sign_up_page.fill_in_password_second_input(password)
        sign_up_page.click_create_account_button()
        assert (FIRST_PARAGRAPH.format(email) in
                sign_up_page.human_proof_first_paragraph)
