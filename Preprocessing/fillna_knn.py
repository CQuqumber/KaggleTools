from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OneHotEncoder

def fillna_knn(df, base, target, n_neighbors, fraction, threshold=10):
''' Fill NaN by KNN

		Parameters:
		-----------
		df: DataFrame

		base: list

		base: np.ndarray / target: str

		n_neighbors: int

		fraction: float

		Example:  fillna_knn( df = geoprop,
                  			base = [ 'latitude', 'longitude' ] ,
                  			target = 'regionidcity', fraction = 0.15 )
		Return:  
		-----------
	'''
	assert isinstance(base, list) or isinstance(base, np.ndarray) and isinstance(target, str)

	whole = [target] + base

	miss = df[target].isnull()
	notmiss = ~miss
	nummiss = miss.sum()

	enc = OneHotEncoder()
	X_target = df.loc[ notmiss, whole ].sample( frac = fraction )
    
    enc.fit( X_target[ target ].unique().reshape( (-1,1) ) )
    
    Y = enc.transform( X_target[ target ].values.reshape((-1,1)) ).toarray()
    X = X_target[ base  ]
    
    print( 'fitting' )

    clf = KNeighborsClassifier( n_neighbors = n_neighbors, weights = 'uniform' )
    clf.fit( X, Y )
    
    print( 'the shape of active features: ' ,enc.active_features_.shape )
    
    print( 'perdicting' )
    Z = clf.predict(geoprop.loc[ miss, base  ])
    
    numunperdicted = Z[:,0].sum()
    if numunperdicted / nummiss *100 < threshold :
        print( 'writing result to df' )    
        df.loc[ miss, target ]  = np.dot( Z , enc.active_features_ )
        print( 'num of unperdictable data: ', numunperdicted )
        return enc
    else:
        print( 'out of threshold: {}% > {}%'.format( numunperdicted / nummiss *100 , threshold ) )





























