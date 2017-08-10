
import numpy as np
import pandas as pd

def convertType(df):
	'''Save Memory by converting float64 to float32

		Parameters:
		-----------
		values: DataFrame


		Return: Data Frame
		-----------
	'''
	for x, dtype in zip(df.columns, df.dtypes):
		if dtype == np.float64:
			df[c] = df[c].astype(np.float32)

	return df