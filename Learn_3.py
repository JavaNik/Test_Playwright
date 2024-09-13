import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("Здесь был URL")
    page.goto("Здесь был URL")
    expect(page.get_by_role("button")).to_contain_text("Войти")
    expect(page.get_by_label("Авторизация")).to_contain_text("Emai")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
