import numpy as np
import pandas as pd
import seaborn as sns

def good_features_corr(df, ratio, droplist):
	'''print missing value ratio sort by values

		Parameters:
		-----------
		df: DataFrame

		ratio: float
			Show the feature(s) below Threshhold ratio

		droplist: list
			Columns  to be excluded

		Return: HeatMap
		-----------
	'''

    missing_df = df_train.isnull().sum(axis=0).reset_index()
    missing_df.columns = ['column_name', 'missing_count']
    missing_df['missing_ratio'] = missing_df['missing_count'] / df_train.shape[0]
    df_new = missing_df.loc[missing_df['missing_ratio']< ratio]
    df_new = df_train[list(df_new.column_name)].drop(droplist, axis=1)
    corrmat = df_new.corr()
    f, ax = plt.subplots(figsize=(12, 9))
    sns.heatmap(corrmat, vmax=.8, square=True,cmap="YlGnBu")
    plt.show()