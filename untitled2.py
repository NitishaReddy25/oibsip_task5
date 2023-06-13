# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1llq9Sgrqeh1YRS9IYYsU72iIHapkQlKx
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv("/content/Advertising.csv")

df.head()

df.shape

df.columns.values.tolist()

df.info()

df.describe()

df=df.drop(columns=["Unnamed: 0"])

df

x=df.iloc[:, 0:-1]

x

y=df.iloc[:,-1]

y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=43)

x_train

x_test

y_train

y_test

x_train=x_train.astype(int)
y_train=y_train.astype(int)
x_test=x_test.astype(int)
y_test=y_test.astype(int)

from sklearn.preprocessing import StandardScaler
Sc=StandardScaler()
x_train_scaled=Sc.fit_transform(x_train)
x_test_scaled=Sc.fit_transform(x_test)

from sklearn.linear_model import LinearRegression

lr=LinearRegression()

lr.fit(x_train_scaled,y_train)

y_pred=lr.predict(x_test_scaled)

from sklearn.metrics import r2_score

r2_score(y_test,y_pred)

import matplotlib.pyplot as plt

plt.scatter(y_test,y_pred,c='g')

from google.colab import drive
drive.mount('/content/drive')