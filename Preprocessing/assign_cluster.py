import numpy as np 
import pandas as pd 
import pickle 
from sklearn.cluster import KMeans

def assign_cluster(df, n_clusters, feature, featurename, savemodel=True, filename):
''' 	K-Means clustering without prediction

		Parameters:
		-----------
		df: DataFrame

		n_clusters: int

		feature: list

		featurename: str

		savemodel: boolean

		filename: str

		Example: date_variable(df, 'timestamp')
		-----------
	'''
	kmeans = KMeans(n_clusters = n_clusters).fit(df[feature])
	df.loc[:, name] = kmeans.labels_
	if savemodel:
		pickle.dump(kmeans, open(filename, 'wb'))

	return df
