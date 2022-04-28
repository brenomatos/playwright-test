import asyncio
import time
from playwright.async_api import async_playwright

power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiMzk4ZWFhYmYtMjdjMC00Yzk4LTkxNTAtNzM2MzM0YTAwYWE0IiwidCI6IjdmNWY0YjY0LTcwZDAtNDMwZi1iMDc2LWE0ODg2MmI4NjUxOCJ9"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False,slow_mo=2000)
        page = await browser.new_page()
        await page.goto(power_bi_url)

        await page.screenshot(path="example.png")
        selector = "visual-container.visual-container-component:nth-child(8) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > visual-modern:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4)"
        
        await page.hover(selector)
        # iframe = page.locator(selector)

        html = str(await page.inner_html(selector))
        dados_antigos = html
        await page.mouse.wheel(5000,0) #scroll vertical
        while(1):
            await page.mouse.wheel(0,500)

            dados_novos = str(await page.inner_html(selector)) 
            html += dados_novos
            if(dados_novos != dados_antigos):
                dados_antigos = dados_novos
            else:
                break
        print(html)

        await browser.close()

asyncio.run(main())