文件介绍：
preprocessing.py:数据后续处理模块
main.py:主程序，实现了8种方式，6种算法预测房价
		使用方式：python main.py 参数
		参数可以是：li :线性回归
					la :lasso回归
					lc :lasso的变体lassocv
					llc :lasso的变体lassolarscv
					p :PassiveAggressive回归
					m :MLP
					b :贝叶斯岭算法
					rf :随机森林
		其中调用的my_shuffle函数的train_set_rate参数可以改变，但不宜过小
test_jitter.py：测试MLP抖动
test_randomforest_depth.py：测试随机森林的预测结果与最大深度的关系
test_mlp_struct.py：测试MLP的结构对测试结果的影响
data.csv：之前处理好的数据
result_trainRate0.99:训练集占比0.99时预测结果的数据