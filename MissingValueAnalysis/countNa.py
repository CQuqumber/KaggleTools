import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

def countNa(df):
	'''Do barplot of missing values / NaN

		Parameters:
		-----------
		values: Pandas Data Frame

		Return: Pandas Data Frame
		-----------

	'''
	null_value = df.isnull().sum().reset_index()
	null_value.columns = ['feature','countNA']
	null_value = null_value.sort_values('countNA', ascending = False)
	fig, ax = plt.subplots()
	fig.set_size_inches(11,15)
	graph = sns.barplot('countNA', 'feature', data = null_value, ax = ax)
	graph.set(xlabel = 'Count of NA values', ylabel = 'Features')
	plt.show()