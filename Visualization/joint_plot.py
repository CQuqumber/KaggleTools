import numpy as np
import pandas as pd
import seaborn as sns

def jointplot(train_df, uplimit, lolimit, xvar, yvar, xlabel, ylabel, mask):
	'''Join Plot for 

		Parameters:
		-----------
		df: DataFrame

		uplimit: float
			Percentile upper bound

		lolimit: float
			Percentile lower bound

		xvar: str
			variable name in x-axis

		yvar: str
			variable name in y-axis

		xlabel: str
			xlabel name

		ylabel: str
			ylabel name

		mask: boolean
			Boolean mask for replacement,
			True: exclude
			False: replace
			--------------
			if True exclude the up/lo bound value by boolean mask,
			if False the value over/below the uplimit/lolimit replace them with value of uplimit/lolimit


		color_num: int, default = 4
			The number in sns.color_palette()

		Return: HeatMap
		-----------
	'''
    median_values = train_df.median(axis=0)
    train_df = train_df.fillna(median_values, inplace=True)
    ulimit = np.percentile(train_df[xvar].values, uplimit)
    llimit = np.percentile(train_df[xvar].values, lolimit)
    if mask == True:
        train_df[xvar] = train_df[xvar].ix[train_df[xvar]<ulimit]
        train_df[xvar] = train_df[xvar].ix[train_df[xvar]>llimit]
    else:
        train_df[xvar].ix[train_df[xvar]>ulimit] = ulimit
    	train_df[xvar].ix[train_df[xvar]<llimit] = llimit

    plt.figure(figsize=(12,12))
    sns.jointplot(x=train_df[xvar].values, y=train_df[yvar].values, size=10, kind='hex',color="#34495e")
    plt.ylabel(ylabel, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    #plt.title("Finished square feet 12 Vs Log error", fontsize=15)
    plt.show()