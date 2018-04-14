# -*- coding: utf-8 -*-
"""
Created on 2018/3/22 14:31

@file: 360.py
@author: Qingyu Mao
"""
import requests
from bs4 import BeautifulSoup

querystring = {"page": 1}
url = "http://zhushou.360.cn/list/index/cid/1"
for i in range(1, 25):
    querystring["page"] = i
    html_doc = requests.request("GET", url, params=querystring)
    soup = BeautifulSoup(html_doc.content, "lxml")
    a_list = soup.select("#iconList > li > a.dbtn")
    for a in a_list:
        print(a.attrs["href"].split("&url=")[1])
