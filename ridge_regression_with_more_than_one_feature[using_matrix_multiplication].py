# -*- coding: utf-8 -*-
"""Ridge_Regression with more than one feature[Using matrix multiplication].ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k1qr9P5CKLZHebNdCMhgAny9KW9aieFG
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

X,y=make_regression(n_samples=100,n_features=4,n_informative=4,n_targets=1,noise=20,random_state=3)

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=4,test_size=0.33)

print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

R0=Ridge(alpha=2)

R0.fit(X_train,y_train)

R0.score(X_test,y_test)

print(R0.intercept_,R0.coef_)

class MeraRidge:
    def __init__(self,alpha):
        self.intercept=None
        self.m=None
        self.alpha=alpha
    def fit(self,X_train,y_train):
        X_train=np.insert(X_train,0,1,axis=1)
        I=np. identity(X_train.shape[1], dtype = None) 
        beta=np.linalg.inv(np.dot(X_train.T,X_train)+self.alpha*I).dot(X_train.T).dot(y_train)
        self.intercept=beta[0]
        self.m=beta[1:]
        print(self.intercept,self.m)

R1=MeraRidge(0)

R1.fit(X_train,y_train)

