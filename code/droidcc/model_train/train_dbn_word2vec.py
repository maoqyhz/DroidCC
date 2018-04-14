# -*- coding: utf-8 -*-
"""
Created on 2018/3/30 13:52

@file: train_dbn.py
@author: Qingyu Mao
"""
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.metrics.classification import accuracy_score
import pandas as pd
from dbn.tensorflow import SupervisedDBNClassification

np.random.seed(1337)  # for reproducibility

# SAMPLE_360 = "D:\\Coding\\Workspace\\PycharmProjects\\malware_detection\\360sample_word2vec.csv"
# APKPURE = "D:\\Coding\\Workspace\\PycharmProjects\\malware_detection\\apkpure_word2vec.csv"
# MALICIOUS = "D:\\Coding\\Workspace\\PycharmProjects\\malware_detection\\malicious_word2vec.csv"
#
# sample_360 = pd.read_csv(SAMPLE_360)
# apkpure = pd.read_csv(APKPURE)
# malicious = pd.read_csv(MALICIOUS)
#
# dataset = pd.concat([sample_360, apkpure, malicious], ignore_index=True)

#
# def foo(x):
#     if x == 1:
#         return "m"
#     else:
#         return "b"
#
#
# dataset['label'] = dataset['label'].map(lambda x: foo(x))
# dataset.to_csv("sample-3000_word2vec_weka.csv", index=False)

dataset = pd.read_csv("../data/sample-3000_word2vec.csv")
X = dataset.drop("label", 1)
Y = dataset["label"]
# # Splitting data
X_train, X_test, Y_train, Y_test = train_test_split(X.values, Y.values, test_size=0.5, random_state=0)


# Training
"""
 :param hidden_layers_structure:     隐层大小
 :param learning_rate_rbm:           预训练阶段的学习率
 :param learning_rate:               微调阶段的学习率
 :param n_epochs_rbm:                进行预训练的迭代次数
 :param n_iter_backprop:             进行训练的迭代次数
 :param batch_size:                  minibatch的大小
 :param activation_function:         激励函数
 :param dropout_p:
"""
classifier = SupervisedDBNClassification(hidden_layers_structure=[250, 250],
                                         learning_rate_rbm=0.05,
                                         learning_rate=0.1,
                                         n_epochs_rbm=10,
                                         n_iter_backprop=100,
                                         batch_size=50,
                                         activation_function='relu',
                                         dropout_p=0.2)
classifier.fit(X_train, Y_train)

# Test
Y_pred = classifier.predict(X_test)
print('Done.\nAccuracy: %f' % accuracy_score(Y_test, Y_pred))

print("=== Detailed Accuracy By Class ===\n")
print(classification_report(Y_test, Y_pred, digits=3))
print("=== Confusion Matrix ===\n")
print(confusion_matrix(Y_test, Y_pred))
print(roc_auc_score(Y_test, Y_pred))


# import matplotlib.pyplot as plt
# from sklearn.metrics import roc_curve, auc
#
# # y_test：实际的标签, dataset_pred：预测的概率值。
# fpr, tpr, thresholds = roc_curve(Y_test, Y_pred)
# roc_auc = auc(fpr, tpr)
# # 画图，只需要plt.plot(fpr,tpr),变量roc_auc只是记录auc的值，通过auc()函数能计算出来
# plt.plot(fpr, tpr, lw=1, label='ROC(area = %0.3f)' % (roc_auc))
# plt.xlabel("FPR (False Positive Rate)")
# plt.ylabel("TPR (True Positive Rate)")
# plt.title("Receiver Operating Characteristic, ROC(AUC = %0.2f)" % (roc_auc))
# plt.show()
