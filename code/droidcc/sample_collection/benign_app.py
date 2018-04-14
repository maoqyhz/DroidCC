# -*- coding: utf-8 -*-
"""

从apkpure上分类别爬取benign app

Created on 2018/3/9 16:31

@file: benign_app.py
@author: Qingyu Mao
"""
from bs4 import BeautifulSoup
import codecs
import requests
import time

CATEGORY_FILE_PATH = "benign_app_category.txt"
DOWNLOAD_LINK_PATH = "benign_app_download_link.txt"
BASE_URL = "https://apkpure.com"


def get_url():
    with codecs.open(CATEGORY_FILE_PATH, "r", "utf-8") as f:
        categoty_list = f.read().split("\r\n")
    url_list = map(lambda p: BASE_URL + "/" + p, categoty_list)
    return list(url_list)


def parse():
    urls = get_url()

    querystring = {"page": 1}
    with codecs.open(DOWNLOAD_LINK_PATH, "a") as f:
        for url in urls:
            print(url)
            for i in range(1, 6, 1):
                print("page %d" % i)
                querystring["page"] = i
                html_doc = requests.request("GET", url, params=querystring)
                soup = BeautifulSoup(html_doc.content, "lxml")
                a_list = soup.select("#pagedata > li > div.category-template-down > a")
                outer_urls = []
                for a in a_list:
                    outer_urls.append(BASE_URL + a.attrs["href"])
                for outer_url in outer_urls:
                    inner_doc = requests.request("GET", outer_url)
                    time.sleep(10)
                    s = BeautifulSoup(inner_doc.content, "lxml")
                    download_link = s.select_one("#download_link").attrs["href"]
                    f.write(download_link + "\n")
                    print(s.title)
                print("sleep...")
                time.sleep(120)


if __name__ == '__main__':
    parse()
