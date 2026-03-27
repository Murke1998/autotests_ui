from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле Email
    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле Username
    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill("username")

    # Заполняем поле Password
    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill("password")

    # Нажимаем на кнопку Registration
    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()

    #Проверяем что заголовок Dashboard отображается
    dashboard_page = page.locator('//h6[@data-testid="dashboard-toolbar-title-text"]')
    expect(dashboard_page).to_be_visible()
    expect(dashboard_page).to_have_text("Dashboard")
