#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.neural_network import MLPRegressor
from preprocessing import preprocessing,my_shuffle
filename="data.csv"

x,y = preprocessing(filename=filename)
X_train,Y_train,X_test,Y_test=my_shuffle(x,y,train_set_rate=0.99)

layer_size=[(50,),(50,50),(50,50,50),(100,),(100,100),(100,100,100),(150,),(150,150),(150,150,150),(200,),(200,200),(200,200,200)]
i=0
while i<len(layer_size):
	reg = MLPRegressor(hidden_layer_sizes=(100))

	reg.fit(X_train,Y_train)
	predictions = reg.predict(X_test)
	if reg.score(X_test, Y_test)>0:
		print('R-squared: %.2f' % reg.score(X_test, Y_test))
		i+=1
	else:
		print("erro!")
		exit(-1)
	#result：
	# R-squared: 0.82
	# R-squared: 0.81
	# R-squared: -2.73
	# R-squared: 0.82
	# R-squared: 0.86
	# R-squared: 0.85
	# R-squared: 0.87
	# R-squared: 0.85
	# R-squared: 0.86
	# R-squared: 0.85