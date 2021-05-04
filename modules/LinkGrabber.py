import urllib.request
from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup as Soup

ytsearch_url = "https://www.youtube.com/results?search_query="
video_url = "https://www.youtube.com/watch?v="
google_images_url = "https://www.google.com/search?tbm=isch&q="


def linkcreator(url, id):
    return url + id


def videograbber(searchterm):
    final_url = ytsearch_url + searchterm
    request = urllib.request.urlopen(final_url)
    video_ids = re.findall(r"watch\?v=(\S{11})", request.read().decode())
    return linkcreator(video_url, video_ids[0])


def imagegrabber(searchterm):
    final_url = google_images_url + searchterm
    print(final_url)
    request = Request(final_url, headers = {'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(request)
    html = Soup(webpage, 'html.parser')
    imgs = [img['src'] for img in html.find_all('img')]
    #print(imgs[1])
    return imgs[1]


