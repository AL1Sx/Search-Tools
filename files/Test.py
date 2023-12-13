import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
import requests
import os

async def main():
    search_word = input('>>>')
    url = f'https://www.pixiv.net/artworks/{search_word}'

    browser = await launch(executablePath='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
    page = await browser.newPage()
    await page.goto(url)

    content = await page.content()
    soup = BeautifulSoup(content, 'html.parser')

    elements = soup.find_all(class_='sc-1qpw8k9-3 ilIMcK gtm-expand-full-size-illust')

    for i, element in enumerate(elements):
        img_url = None  # 初始化 img_url
        parent = element.parent
        if 'href' in parent.attrs:
            img_url = parent['href']
        else:
            print('???')
        if img_url is not None:  # 只有当 img_url 不为 None 时，才尝试下载图片
            response = requests.get(img_url)
            with open(os.path.join('images', f'image_{i}.jpg'), 'wb') as f:
                f.write(response.content)
            print(f'Downloaded image_{i}.jpg')

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())