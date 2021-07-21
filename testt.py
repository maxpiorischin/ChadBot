import aiohttp, asyncio
from bs4 import BeautifulSoup as Soup
import requests

REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

async def main():
    async with aiohttp.request('GET', 'https://google.ca', headers=REQUEST_HEADER) as resp:
        text = await resp.read()

    return text


run = asyncio.run(main())
print(type(run))

def other():
    request = requests.get('https://google.ca', headers = REQUEST_HEADER).text
    return request

print(type(other()))
