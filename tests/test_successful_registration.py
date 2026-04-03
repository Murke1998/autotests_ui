import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, username, password",[
    ("user.name@gmail.com", "545","password"),
    ("user.name@gmail.com", "4894","password")
])
def test_successful_registration(registration_page: RegistrationPage, dashboard_page email:str, username:str, password:str):
    registration_page.fill_registration_form(email=email, username=username, password= password)
    registration_page.click_registration_button()
    dashboard_page.