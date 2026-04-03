import pytest
from playwright.sync_api import sync_playwright, Playwright, Page


@pytest.fixture(scope='session')
def initialize_browser_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Переходим на страницу
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        # Заполняем поле Email
        email_input = page.get_by_test_id('registration-form-email-input').locator('//div//input')
        email_input.fill("user.name@gmail.com")

        # Заполняем поле Username
        username_input = page.get_by_test_id('registration-form-username-input').locator('//div//input')
        username_input.fill("username")

        # Заполняем поле Password
        password_input = page.get_by_test_id('registration-form-password-input').locator('//div//input')
        password_input.fill("password")

        # Нажимаем на кнопку Registration
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path="browser-state.json")

@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope='function')
def chromium_page(playwright: Playwright) -> Page:
    page = playwright.chromium.launch(headless=False)
    page = page.new_page()
    yield page
    page.close()
