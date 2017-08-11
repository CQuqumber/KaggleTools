def missingno_matrix(df):
''' Missing Value visualization by matrix plot

		Parameters:
		-----------
		df: DataFrame

		Return: matrix plot
		-----------
	'''
	import seaborn as sns
	import matplotlib.pyplot as plt
	import matplotlib
	matplotlib.style.use('ggplot')
	import missingno as msno

	missingValueColumns = df.columns[df.isnull().any()].tolist()
	msno.matrix(df[missingValueColumns],width_ratios=(10,1),\
            figsize=(20,8),color=(0,0, 0),fontsize=12,sparkline=True,labels=True)
	plt.show()