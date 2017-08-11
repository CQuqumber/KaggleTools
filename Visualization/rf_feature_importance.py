
def importance(train_df, target, droplist, howmany, n_estimators, max_features, max_depth):
	'''Feature Importance by bar plot

		Parameters:
		-----------
		train_df: DataFrame

		target: str
			Show the feature(s) below Threshhold ratio

		droplist: list
			Columns  to be excluded

		howmany: int
			Numbers of features want to show up

		==================================================================
		n_estimators: int
		max_depth: int
		max_features:
			If int, then consider max_features features at each split.
			If float, then max_features is a percentage and int(max_features * n_features) features are considered at each split.
			If “auto”, then max_features=n_features.
			If “sqrt”, then max_features=sqrt(n_features).
			If “log2”, then max_features=log2(n_features).
			If None, then max_features=n_features.
		==================================================================

		Return: barplot
		-----------
	'''


	train_y = train_df[target].values
	train_df = train_df.drop(droplist, axis=1)
	feat_names = train_df.columns.values

	from sklearn import ensemble
	model = ensemble.ExtraTreesRegressor(n_estimators=n_estimators, max_depth=max_depth, max_features=max_features, random_state=0)
	model.fit(train_df, train_y)

	## plot the importances ##
	importances = model.feature_importances_
	std = np.std([tree.feature_importances_ for tree in model.estimators_], axis=0)
	indices = np.argsort(importances)[::-1][:howmany]

	plt.figure(figsize=(12,12))
	plt.title("Feature importances")
	plt.bar(range(len(indices)), importances[indices], color="r", yerr=std[indices], align="center")
	plt.xticks(range(len(indices)), feat_names[indices], rotation='vertical')
	plt.xlim([-1, len(indices)])
	plt.show()