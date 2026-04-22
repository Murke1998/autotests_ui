import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.registration
@pytest.mark.regression
@pytest.mark.parametrize("email, username, password", [
    ("test@gmail.com", "testuser", "Password123"),
])
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage, email:str,
                                 username:str, password:str):
    registration_page.fill_registration_form(email, username, password)
    registration_page.click_registration_button()
    dashboard_page.visible_dashboard_title_text()