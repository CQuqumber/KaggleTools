def xgb_importance(train_df, train_y):
	''' XGB Feature Importance by bar plot

		Parameters:
		-----------
		train_df: DataFrame

		train_y: DataFrame

		Return: barplot
		-----------
	'''
	import xgboost as xgb
	xgb_params = {}
	xgb_params["objective"] = "reg:linear" # reg:logistic,count:poisson
	xgb_params['min_child_weight'] = 100
	xgb_params["eta"] = 0.1
	xgb_params["subsample"] = 0.8
	xgb_params["colsample_bytree"] = 0.7
	xgb_params["max_depth"] = 9
	xgb_params['gamma'] = .01
	xgb_params['tree_method']='exact'
	xgb_params['eval_metric'] = 'rmse'

	xgb_params["silent"] = 1
	xgb_params['verbose'] = 2
	xgb_params['seed'] = 9487
	xgb_params['base_score'] = np.median(train_y)

	dtrain = xgb.DMatrix(train_df, train_y, feature_names=train_df.columns.values)
	model = xgb.train(dict(xgb_params, silent=0), dtrain, num_boost_round=50)

	# plot the important features #
	fig, ax = plt.subplots(figsize=(12,18))
	xgb.plot_importance(model, height=0.8, ax=ax)
	plt.show()