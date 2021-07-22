import aiohttp, asyncio
from bs4 import BeautifulSoup as Soup
import requests

REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

async def main():
    session = aiohttp.ClientSession()
    async with session.get('https://www.urbandictionary.com/define.php?term=Among%20Us', headers=REQUEST_HEADER) as resp:
        text = await resp.text()
    await session.close()
    return text


run = asyncio.run(main())
print(run)
print("amogus")
def other():
    request = requests.get('https://www.urbandictionary.com/define.php?term=Among%20Us', headers = REQUEST_HEADER).text
    return request

print(other())
