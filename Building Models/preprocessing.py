#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import random
import numpy as np
from sklearn.preprocessing import LabelEncoder  
from sklearn.preprocessing import OneHotEncoder  

# 数据预处理
def preprocessing(filename):
	# 以UTF-8格式打开文件
	f=open(filename,encoding='UTF-8')
	rd=csv.reader(f)
	data=list(rd)
	# 转为numpy数组，以便处理
	data=np.array(data)
	f.close()
	#去掉第一行
	data=data[1:]
	data_num=data.shape[0]
	y=data[:,-1]
	data=data[:,:-1]
	#LabelEncoder将字符串转化成数字
	class_le = LabelEncoder()
	#前六列转化成数字，以便转独热码
	for i in range(6):
		data[:, i] = class_le.fit_transform(data[:, i]) 
	#两个布尔型
	data[:,6]=[ 1*(data[i,6]=='有') for i in range(data_num) ]
	data[:,7]=[ 1*(data[i,7]=='交通便利') for i in range(data_num) ]
	new_data=data[:,0:10]
	#padding用来扩充new_data矩阵，以便添加其他数据
	padding=np.array([[None for i in range(11)] for j in range(data_num)])
	new_data=np.append(new_data,padding,axis=1)
	data=data[:,10:]
	for i in range(data_num):
		new_data[i,10]=int(data[i,0][0])
		new_data[i,11]=int(data[i,0][2])
		new_data[i,12]=int(data[i,0][4])

		for j in range(8):
			new_data[i,13+j]=1*(data[i,1].find(str(j))!=-1)
	ohe = OneHotEncoder(categorical_features=list(range(6))) 
	#独热码
	x=ohe.fit_transform(new_data).toarray()  
	x=x.astype('float64')
	y=y.astype('float64')
	y.reshape(-1,1)
	return x,y

#打乱顺序，并分割训练集与测试集
def my_shuffle(x,y,train_set_rate):
	#确保数据的正确性
	assert x.shape[0]==y.shape[0]
	data_num=y.shape[0]
	index=list(range(data_num))
	random.seed(a=None, version=2)
	# 打乱顺序
	random.shuffle(index)
	x=x[index]
	y=y[index]
	rate=train_set_rate
	#分割训练集与测试集
	X_train=x[:int(data_num*rate)]
	X_test=x[int(data_num*rate):]
	Y_train=y[:int(data_num*rate)]
	Y_test=y[int(data_num*rate):]
	return X_train,Y_train,X_test,Y_test