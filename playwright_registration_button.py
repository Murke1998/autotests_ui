from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверка кнопка Registration в состоянии disabled
    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    expect(registration_button).to_be_disabled()

    # Заполняем поле Email
    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле Username
    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill("username")

    # Заполняем поле Password
    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill("password")

    # Проверка кнопка Registration в состоянии enabled
    expect(registration_button).not_to_be_disabled()
