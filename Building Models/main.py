#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.linear_model import LinearRegression,Lasso,LassoCV,LassoLarsCV,PassiveAggressiveRegressor,BayesianRidge,LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from preprocessing import preprocessing,my_shuffle
import sys


if __name__ == '__main__':

	filename="data.csv"
	#预处理
	x,y = preprocessing(filename=filename)

	#打乱顺序，分割训练集与测试集
	X_train,Y_train,X_test,Y_test=my_shuffle(x,y,train_set_rate=0.99)
	#参数数量错误
	if len(sys.argv) !=2 :
		print('argv number erro!')
		exit(-1)
	# 根据参数选择各种不同预测方法
	if sys.argv[1] == 'li':
		reg = LinearRegression()
	elif sys.argv[1] == 'la':
		reg = Lasso(alpha = 0.1)
	elif sys.argv[1] == 'lc':
		reg = LassoCV()  
	elif sys.argv[1] == 'llc':
		reg = LassoLarsCV()
	elif sys.argv[1] == 'p':
		reg = PassiveAggressiveRegressor(random_state=0)
	elif sys.argv[1] == 'm':
		reg = MLPRegressor(hidden_layer_sizes=(100))
	elif sys.argv[1] == 'b':
		reg=BayesianRidge()
	elif sys.argv[1] == 'rf':
		reg =RandomForestRegressor(max_depth=10, random_state=0)
	else :
		#参数错误
		print("argv erro!")
		exit(-2)
	# 训练	
	reg.fit(X_train,Y_train)
	predictions = reg.predict(X_test)
	#打印预测结果与真实结果
	for i, prediction in enumerate(predictions):
	    print('Predicted: %s, Target: %s' % (prediction, Y_test[i]))
	#打印R-squared
	print('R-squared: %.2f' % reg.score(X_test, Y_test))