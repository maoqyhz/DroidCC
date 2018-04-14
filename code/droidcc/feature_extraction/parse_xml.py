# -*- coding: utf-8 -*-
"""
Created on 2018/3/13 15:10

parse permissions and intent-filter action from AndroidManifest.xml

@file: parse_xml.py
@author: Qingyu Mao
"""
from xml.etree.ElementTree import parse
import codecs

import os

BASE_PATH = "D:\\Coding\\Workspace\\IdeaProjects\\maldetect\\unpacked\\"
# BASE_PATH = "J:\\dataset\\malicious\\"
FILE_NAME = "AndroidManifest.xml"
NAMESPACE = '{http://schemas.android.com/apk/res/android}'

apks = os.listdir(BASE_PATH)
count = 1
for apk in apks:
    print("%d - %s" % (count, apk))
    count = count + 1
    tmp_path = os.path.join(os.path.join(BASE_PATH, apk), FILE_NAME)
    try:
        tree = parse(tmp_path)
        root = tree.getroot()
        with codecs.open("../data/static/malicious/virusTotal/" + apk + ".txt", "a") as f:
            for elem in tree.iter("uses-permission"):
                permission = elem.attrib[NAMESPACE + "name"]
                permission_str = permission.split("permission.")
                if len(permission_str) > 1:
                    f.write("permission." + elem.attrib[NAMESPACE + "name"].split("permission.")[1] + "\n")
            for elem in tree.iter("action"):
                f.write(elem.attrib[NAMESPACE + "name"] + "\n")
    except FileNotFoundError as e:
        with codecs.open("error", "a") as ee:
            ee.write(apk + "\n")
