def dataType(df):
''' LightGBm Feature Importance by bar plot

		Parameters:
		-----------
		df: DataFrame

		Return: sns barplot
		-----------

	'''
	import seaborn as sns
	import matplotlib.pyplot as plt
	matplotlib.style.use('ggplot')
	dataTypeDf = pd.DataFrame(df.dtypes.value_counts()).reset_index().rename(columns={"index":"variableType",0:"count"})
	fig, ax = plt.subplots()
	fig.set_size_inches(20,5)
	sns.barplot(data=dataTypeDf,x="variableType",y="count",ax=ax,color="#34495e")
	ax.set(xlabel='Variable Type', ylabel='Count',title="Variables Count Across Datatype")
	plt.show()