# -*- coding: utf-8 -*-
"""Mini_batch Stochastic Gradient.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mNYsnx_autQPjYraPyAfC1g6tScBM2F5
"""

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import random

X,y=make_regression(n_samples=100,n_features=3,n_informative=3,n_targets=1,noise=40)

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=4)

X_train.shape

X_test.shape

l=LinearRegression()
l.fit(X_train,y_train)

y_pred1=l.predict(X_test)

print(l.intercept_,l.coef_)

r2_score(y_test,y_pred1)

class Mini_batch_gradient:
    def __init__(self,batch,lr,epoch):
        self.batch=batch
        self.lr=lr
        self.epoch=epoch
        self.coff=np.ones(X_train.shape[1])
        self.intercept=0
    def fit(self,X_train,y_train):

        for i in range(self.epoch):
            
            for j in range(int(X_train.shape[0]/self.batch)):

                idx=random.sample(range(0,X_train.shape[0]),self.batch)

                y_hat=np.dot(X_train[idx],self.coff)+self.intercept
                
                intercept_der=-2*np.mean(y_train[idx]-y_hat)

                self.intercept=self.intercept-self.lr*intercept_der

                cof_der=-2*np.dot((y_train[idx]-y_hat),X_train[idx])/self.batch

                self.coff=self.coff-self.lr*cof_der
        print(self.intercept,self.coff)
    def predict(self,X_test):
        return np.dot(X_test,self.coff)+self.intercept

g=Mini_batch_gradient(25,0.1,100)

g.fit(X_train,y_train)

y_pred=g.predict(X_test)

r2_score(y_pred,y_test)



