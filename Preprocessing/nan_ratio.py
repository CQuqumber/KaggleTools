import numpy as np 
import pandas as pd 

def nan_ratio(df,ratio):
	'''print missing value ratio sort by values

		Parameters:
		-----------
		df: DataFrame

		ratio: float
			Show the feature(s) over Threshhold ratio

		Return: Data Frame
		-----------
	'''
	missing_df = df.isnull().sum(axis=0).reset_index()
	missing_df.columns = ['column_name', 'missing_count']
	missing_df['missing_ratio'] = missing_df['missing_count'] / df.shape[0]
	missing_df.ix[missing_df['missing_ratio']>ratio]
	return missing_df.loc[missing_df['missing_ratio']>ratio].sort_values(by='missing_ratio', ascending=False)