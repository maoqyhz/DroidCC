# coding: utf-8

# In[12]:


import gensim
import logging
import numpy as np
import codecs
from time import time
import os

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# In[13]:


PATH = "test_data.txt"
BASE_PATH = "static\\benign\\apkpure - 1000\\"
FEATURE_PATH = "features.txt"


def get_feature_list():
    """
    获取所有已知的特征集合
    :return: 
    """
    with codecs.open(FEATURE_PATH, "r") as f:
        feature_list = f.read().split("\n")
    return feature_list


def clean_intent(x):
    """
    处理intent-filter action
    :param x: 
    :return: 
    """
    # 格式处理
    t = x.split("intent.")
    if len(t) > 1:
        return t[1]
    else:
        return x


def preprocessing(path):
    """
    特征预处理
    
    根据提取的三类特征分为三个sentences，在分词
    """
    with codecs.open(path, "r", encoding="utf-8") as f:
        content_list = f.read().split("\r\n")
    content_list = list(map(clean_intent, content_list))
    # 去除不在特征列表中的特征
    new_content_list = []
    features = get_feature_list()
    for feature in content_list:
        if feature in features:
            new_content_list.append(feature)
    s1, s2, s3 = [], [], []
    for ff in new_content_list:
        if "permission" in ff:
            s1.append(ff)
            continue
        if "action" in ff:
            s2.append(ff)
            continue
        s3.append(ff)
    sentences = [s1, s2, s3]
    return sentences


apks = os.listdir(BASE_PATH)
apks_vec_features = []
features = get_feature_list()
for apk in apks:
    print(apk)
    real_path = os.path.join(BASE_PATH, apk)
    sentences = preprocessing(real_path)
    try:
        model = gensim.models.Word2Vec(sentences, sg=1, size=100, window=3, min_count=1)
    except RuntimeError as e:
        print(e.__class__)
        pass
    L = []
    empty_feature = [0 for i in range(100)]
    for f in features:
        if f in model.wv.vocab:
            L.extend(model.wv[f])
        else:
            L.extend(empty_feature)
    L.append(0)
    apks_vec_features.append(L)

columns = []
for ff in features:
    for i in range(100):
        columns.append("%s-%s" % (ff, i))
columns.append("label")

import pandas as pd

df = pd.DataFrame(apks_vec_features, columns=columns)
# df = df.iloc[:1500, :]
print(df.iloc[:, 0].size)
print(df.columns.size)
df.to_csv("apkpure_word2vec.csv", index=False)
