
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
	for c, dtype in zip(df.columns, df.dtypes):
		if dtype == np.float64:
			df[c] = df[c].astype(np.float32)
		elif dtype == np.int64:
			df[c] = df[c].astype(np.int32)

	return df