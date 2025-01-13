import os
import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

page_name = "google"
data_folder = "data"

async def scrape_all(headless=True):
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=headless)
        context = await browser.new_context()
        page = await context.new_page()
        await stealth_async(page)

        await page.goto("https://google.nl")
        await page.wait_for_timeout(3000)

        html_content = await page.content()

        file_name = f"{data_folder}/{page_name}.html"
        os.makedirs(data_folder, exist_ok=True)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(html_content)

        await browser.close()

asyncio.run(scrape_all(headless=True))