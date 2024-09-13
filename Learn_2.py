from playwright.async_api import async_playwright
from pytest_playwright.pytest_playwright import playwright
import asyncio


async def run_playwright():
    async with async_playwright() as p:
        # Запускаем браузер в не headless режиме
        #browser = p.chromium.launch(headless=False)
        browser = await p.chromium.launch(channel='chrome', headless=False)
        page = await browser.new_page()

        # Переход на страницу авторизации
        await page.goto('Здесь был URL')

        # Заполнение полей формы
        await page.fill('input[type="email"]', 'Здесь был email')  # Замените на актуальный селектор
        await page.fill('input[type="password"]', 'Здесь был пароль')  # Замените на актуальный селектор

        # Отправка формы (например, нажатие кнопки "Войти")
        await page.click('button[type="submit"]')  # Замените на актуальный селектор

        # Ждем, пока страница загрузится (можно использовать `wait_for_load_state`)
        await page.wait_for_load_state("networkidle")

        # Переход на страницу, где нужно искать элементы
        await page.goto('https://vk.com/')  # Замените на актуальный URL

        # Ждем, пока страница загрузится (можно использовать `wait_for_load_state`)
        await page.wait_for_load_state("networkidle")

        # Пример поиска элементов на странице
        elements = await page.query_selector_all('span.ant-tag')  # Замените на актуальный селектор

        await page.screenshot(path='scr/demo.png')

        for element in elements:
            print(await element.inner_text())  # Печатает текст каждого найденного элемента

        # Закрываем браузер
        await browser.close()


# Запускаем функцию
asyncio.run(run_playwright())
