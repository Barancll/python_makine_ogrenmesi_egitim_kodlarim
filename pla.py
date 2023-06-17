# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('Wine.csv')
print(veriler)

x = veriler.iloc[:,0:13].values
y = veriler.iloc[:,13].values


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=0)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

#PCA
from sklearn.decomposition import PCA
pca = PCA(n_components= 2)

X_train2 = pca.fit_transform(X_train)
X_test2 = pca.transform(X_test)


from sklearn.linear_model import LogisticRegression

#pca dönüşümünden önce gelen LR
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)

#pca dönüşümünden sonra gelen LR
classifier2 = LogisticRegression(random_state=0)
classifier2.fit(X_train2,y_train)

#tahmin
y_pred = classifier.predict(X_test)

y_pred2 = classifier2.predict(X_test2)


from sklearn.metrics import confusion_matrix

#actual/PCA olmadan çıkan sonuç
print('gercek/PCAsız')
cm = confusion_matrix(y_test,y_pred)
print(cm)

#actual/PCA sonrası çıkan sonuç
print('gercek/PCA ile')
cm2 = confusion_matrix(y_test,y_pred2)
print(cm)

#PCA sonrası/PCA öncesi
print('PCAsız ve PCAlı')
cm3 = confusion_matrix(y_pred,y_pred2)
print(cm)

 





