def date_variable(df, time_col):
''' 	More information: 

		https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DatetimeIndex.weekofyear.html

		Parameters:
		-----------
		df: DataFrame

		time_col: str

		Example: date_variable(df, 'timestamp')
		-----------
	'''
	df[time_col] = pd.to_datetime(df[time_col])
	df['year'] = df[time_col].dt.year
	df['month'] = df[time_col].dt.month
	df['day'] = df[time_col].dt.day
	df['dayofweek'] = df[time_col].dt.dayofweek
	df['days_in_month'] = df[time_col].dt.days_in_month
	df['weekofyear'] = df[time_col].dt.weekofyear































