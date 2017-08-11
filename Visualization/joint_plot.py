import numpy as np
import pandas as pd
import seaborn as sns

def jointplot(df, uplimit=99.5, lolimit=0.5, xvar, yvar, xlabel, ylabel, mask = True, color_num = 4):
	'''Join Plot for 

		Parameters:
		-----------
		df: DataFrame

		uplimit: float, default = 99.5
			Percentile upper bound

		lolimit: float, default = 0.5
			Percentile lower bound

		xvar: str
			variable name in x-axis

		yvar: str
			variable name in y-axis

		xlabel: str
			xlabel name

		ylabel: str
			ylabel name

		mask: boolean, default = True
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
	color = sns.color_palette()
	ulimit = np.percentile(train_df[col].values, uplimit)
	llimit = np.percentile(train_df[col].values, lolimit)
	if mask == True:
		train_df = train_df[col].ix[train_df[col]<ulimit]
		train_df = train_df[col].ix[train_df[col]>llimit]
	else:
		train_df[col].ix[train_df[col]>ulimit] = ulimit
		train_df[col].ix[train_df[col]<llimit] = llimit

	plt.figure(figsize=(12,12))
	sns.jointplot(x=train_df[xvar].values, y=train_df[yvar].values, size=10, color=color[color_num])
	plt.ylabel(ylabel, fontsize=12)
	plt.xlabel(xlabel, fontsize=12)
	#plt.title("Finished square feet 12 Vs Log error", fontsize=15)
	plt.show()	