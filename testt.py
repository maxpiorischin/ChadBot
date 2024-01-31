import asyncio, aiohttp, re

REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

ytsearch_url = "https://www.youtube.com/results?search_query="


async def videograbber(searchterm):
    final_url = ytsearch_url + searchterm
    session = aiohttp.ClientSession()
    async with session.get(final_url,
                           headers=REQUEST_HEADER) as resp:
        text = await resp.text()
    await session.close()
    video_ids = re.findall(r"watch\?v=(\S{11})", text)

asyncio.run(videograbber("roblox"))