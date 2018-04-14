# -*- coding: utf-8 -*-
"""
Created on 2018/3/14 14:03

parse sensitive api from smali code

@file: parse_smali.py
@author: Qingyu Mao
"""
import os
import codecs

PATH = "D:\\Coding\\Workspace\\IdeaProjects\\maldetect\\unpacked\\"
# PATH = "C:\\Users\\Fururur\\Desktop\\apks"
SENSITIVE_API = "../data/sensitive_api.txt"
KEY = "smali"


def get_sensitive_api_list():
    with codecs.open(SENSITIVE_API) as f:
        return f.read().split("\n")


def get_all_files(path):
    files = []
    for dir_path, dir_names, file_names in os.walk(path):
        for name in file_names:
            if KEY in os.path.join(dir_path, name):
                files.append(os.path.join(dir_path, name))
    return files


def find_sapi_in_code(f):
    matches = []
    sapi_list = get_sensitive_api_list()
    for file in f:
        with codecs.open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for api in sapi_list:
            if api in code:
                matches.append(api)
    return matches


if __name__ == '__main__':
    apks = os.listdir(PATH)
    # with codecs.open("error", encoding="utf-8") as ff:
    #     apks = ff.read().split("\r\n")
    for apk in apks:
        print(apk)
        tmp_path = os.path.join(PATH, apk)
        smali_files = get_all_files(tmp_path)
        ss = []
        try:
            ss = find_sapi_in_code(smali_files)
        except (FileNotFoundError, UnicodeDecodeError, UnicodeEncodeError, UnboundLocalError) as e:
            print(e)
            with codecs.open("error", "a") as fe:
                fe.write(apk + "\n")
        print(ss)
        print("-------------------------------------------------")
        with codecs.open("../data/static/malicious/virusTotal/" + apk + ".txt", "a") as f:
            for s in ss:
                f.write(s + "\n")
