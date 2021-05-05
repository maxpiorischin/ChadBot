import urllib.request
from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup as Soup
from googlesearch import search
from selenium import webdriver
import os

ytsearch_url = "https://www.youtube.com/results?search_query="
video_url = "https://www.youtube.com/watch?v="
google_images_url = "https://www.google.co.in/search?q="
google_images_url_end = "&source=lnms&tbm=isch"
google_url = "https://www.google.ca/search?q="

extensions = { "jpg", "jpeg", "png", "gif" }

REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}


def get_soup(url, header):
    return Soup(urlopen(Request(url, headers=header)), 'html.parser')


def linkcreator(url, id):
    return url + id


def videograbber(searchterm):
    final_url = ytsearch_url + searchterm
    request = urllib.request.urlopen(final_url)
    video_ids = re.findall(r"watch\?v=(\S{11})", request.read().decode())
    return linkcreator(video_url, video_ids[0])


def imagegrabber(searchterm, driver):

    url = google_images_url + searchterm + google_images_url_end
    driver.get(url)
    html = driver.page_source.split('["')
    imges = []
    for i in html:
        if i.startswith('http') and i.split('"')[0].split('.')[-1] in extensions:
            imges.append(i.split('"')[0])
            break
    driver.quit()
    return imges[0]

def smallimagegrabber(searchterm):
    final_url = google_images_url + searchterm +google_images_url_end
    print(final_url)
    html = get_soup(final_url, REQUEST_HEADER)
    imgs = [img['src'] for img in html.find_all('img')]
    # print(imgs[1])
    return imgs[1]

def googlesearch(searchterm):
    result = search(searchterm, num_results=3)
    return result[0]
