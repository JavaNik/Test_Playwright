import time

from playwright.sync_api import sync_playwright


def sync_work():
    # открыть соединение
    with sync_playwright() as p:
        # инициализация браузера (без видимого открытия браузера)
        # browser = p.chromium.launch()

        # инициализация браузера (с явным открытием браузера)
        browser = p.chromium.launch(headless=False)
        # инициализация страницы
        page = browser.new_page()
        # переход по url адресу:
        page.goto('ТУТ БЫЛ URL')
        # сделать скриншот
        page.screenshot(path='scr/demo.png')

        browser.close()


sync_work()