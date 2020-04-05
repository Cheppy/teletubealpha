import requests
import wget
from bs4 import BeautifulSoup
import youtube_dl

import os




def get_pic(link):
    resp = requests.get(link)
    soup = BeautifulSoup(resp.text, 'lxml')

    for x in soup.find_all("meta", property="og:image"):
        return x['content']


def show_pic(url):
    imb = wget.download(get_pic(url))
    return imb


def is_size_ok(path, max_allowed=5e7):
    return os.path.getsize(path) < max_allowed


def get_vid(url, content_type):

    ydl_opts = content_type[0]

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        result = ydl.extract_info(url, download=False)
        outfile = ydl.prepare_filename(result)[:-1] + content_type[1]

    return str(outfile)
