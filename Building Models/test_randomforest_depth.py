#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.linear_model import LinearRegression,Lasso,LassoCV,LassoLarsCV,PassiveAggressiveRegressor,BayesianRidge,LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from preprocessing import preprocessing,my_shuffle
filename="data.csv"

x,y = preprocessing(filename=filename)


X_train,Y_train,X_test,Y_test=my_shuffle(x,y,train_set_rate=0.90)

for i in range(2,40):
	reg =RandomForestRegressor(max_depth=i, random_state=0)
	reg.fit(X_train,Y_train)
	predictions = reg.predict(X_test)
	print('R-squared: %.2f' % reg.score(X_test, Y_test))