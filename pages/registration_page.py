from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_button = page.get_by_test_id("registration-page-registration-button")

    def fill_registration_form(self, email:str, username:str, password:str):
        self.page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_registration_button(self):
        self.registration_button.click()

