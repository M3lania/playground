import pytest

INVALID_LOCATION = "No Geocoding Results from this text in the region of World."


class TestHomePageElements:
    pass


class TestHomePageErrors:
    @pytest.mark.parametrize("value", ["1193653471", "Lorem ipsum"])
    def test_location_with_invalid_input(self, homepage_class, value):
        """
        Examples of tests which run in the same browser session. We get speed,
        but lose their independence of each other. To get to the initial state,
        the Geocode menu button is pressed at the end of each test.
        """
        homepage_class.fill_in_location(value)
        homepage_class.click_next_button()
        assert INVALID_LOCATION in homepage_class.location_error
        homepage_class.click_geocode_menu_button()
