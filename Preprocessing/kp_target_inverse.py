import numpy as np


def boxcox_inverse(values, lam):
	'''Inverse the values from box-cox transform, for those

		Parameters:
		-----------
		values: Pandas Series / Numpy Array
				Target values
		lam : float
				Lambda values return by boxcox transform

				Example: 
					from scipy.stats import boxcox
					values, lambda = boxcox(train['y'].values)
		Return
		-----------
		Numpy Array
	'''
    if lam == 0:
        return np.exp(values)
    return np.exp(np.log(lam * values + 1) / lam)

