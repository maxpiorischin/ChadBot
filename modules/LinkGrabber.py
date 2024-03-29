import urllib.request
import aiohttp, asyncio
import re
from bs4 import BeautifulSoup as Soup
from googlesearch import search

ytsearch_url = "https://www.youtube.com/results?search_query="
video_url = "https://www.youtube.com/watch?v="
google_images_url = "https://www.google.co.in/search?q="
google_images_url_end = "&source=lnms&tbm=isch"
google_url = "https://www.google.ca/search?q="
urban_dict_url = "https://www.urbandictionary.com/define.php?term="

extensions = {"jpg", "jpeg", "png", "gif"}

REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}


async def get_soup(url, header, issoup):
    session = aiohttp.ClientSession()
    async with session.get(url,
                           headers=header) as resp:
        text = await resp.text()
    await session.close()
    if issoup:
        return Soup(text, 'html.parser')
    return text


def filter_videos(video_ids, number):
    links = [video_url + video_ids[0]]
    i = 1
    while i < number:
        if video_ids[i] != video_ids[i-1]:
            link = video_url + video_ids[i]
            links.append(link)
        else:
            number += 1
        i += 1
    return links



async def videograbber(searchterm, number):
    final_url = ytsearch_url + searchterm
    text = await get_soup(final_url, REQUEST_HEADER, False)
    video_ids = re.findall(r"watch\?v=(\S{11})", text)
    return filter_videos(video_ids, number)


async def smallimagegrabber(searchterm):
    final_url = google_images_url + searchterm + google_images_url_end
    print(final_url)
    html = await get_soup(final_url, REQUEST_HEADER, True)
    imgs = [img['src'] for img in html.find_all('img')]
    return imgs[1]


async def googlesearch(searchterm):
    result = search(searchterm, num_results=3)
    return result[0]


async def defingrabber(searchterm):
    final_url = urban_dict_url + searchterm
    soup = await get_soup(final_url, REQUEST_HEADER, True)
    return soup.find("div", attrs={"class": "meaning"}).text  # definition
