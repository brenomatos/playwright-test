import asyncio
from playwright.async_api import async_playwright

power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiMzk4ZWFhYmYtMjdjMC00Yzk4LTkxNTAtNzM2MzM0YTAwYWE0IiwidCI6IjdmNWY0YjY0LTcwZDAtNDMwZi1iMDc2LWE0ODg2MmI4NjUxOCJ9"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False,)
        page = await browser.new_page()
        await page.goto(power_bi_url)

        await page.screenshot(path="example.png")
        selector = "#pvExplorationHost > div > div > exploration > div > explore-canvas > div > div.canvasFlexBox > div > div.displayArea.disableAnimations.fitToPage > div.visualContainerHost > visual-container-repeat > visual-container:nth-child(8) > transform > div > div.visualContent > div > visual-modern > div > div > div.tableEx"
        iframe = page.locator(selector)
        print(await iframe.inner_html())

        await browser.close()

asyncio.run(main())