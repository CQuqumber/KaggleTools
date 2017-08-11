def missing_bar(df):
''' Missing Value visualization by bar plot

		Parameters:
		-----------
		df: DataFrame

		Return: sns barplot
		-----------
	'''
	missingValueColumns = df.columns[df.isnull().any()].tolist()
	msno.bar(df[missingValueColumns],figsize=(20,8),color="#34495e",fontsize=12,labels=True)
	plt.show()