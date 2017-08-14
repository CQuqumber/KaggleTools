def get_stats(df, group_col, target_col, drop_raw_col=False):
'''  merge basic stats columns

	Parameters:
	-----------
		df: DataFrame

		group_col: list

		target_col: list

		drop_raw_col: Boolean

		Example: df_new = get_stats_target(df_new, ['sub_area'], ['kitch_sq'])

		Return:  DataFrame
	-----------
	'''

    df_old = df.copy()
    grouped = df_old.groupby(group_col)
    the_stats = grouped[target_col].agg(['mean','median','max','min','std']).reset_index()

    the_stats.columns = [group_col[0],
                       '_%s_mean_by_%s' % (target_col[0], group_col[0]),
                       '_%s_median_by_%s' % (target_col[0], group_col[0]),
                       '_%s_max_by_%s' % (target_col[0], group_col[0]),
                       '_%s_min_by_%s' % (target_col[0], group_col[0]),
                       '_%s_std_by_%s' % (target_col[0], group_col[0])]

    df_old = pd.merge(left=df_old, right=the_stats, on=group_col, how='left')
    if drop_raw_col:
        df_old.drop(group_col, axis=1, inplace=True)
    return df_old