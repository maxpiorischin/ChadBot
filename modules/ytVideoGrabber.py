import urllib.request
import re

search_url = "https://www.youtube.com/results?search_query="
video_url = "https://www.youtube.com/watch?v="

def videolinkcreator(id):
    return video_url + id

def videograbber(searchterm):
    final_url = search_url + searchterm
    request = urllib.request.urlopen(final_url)
    video_ids = re.findall(r"watch\?v=(\S{11})", request.read().decode())
    return videolinkcreator(video_ids[0])
