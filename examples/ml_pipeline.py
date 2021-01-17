import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.svm import SVR

from magicparams import MagicParams

if __name__ == '__main__':

    params = MagicParams(clf='lr', metric='mae').copy_from_argparser()

    print(params)
    X = np.array(list(range(100))).reshape((-1, 1))
    y = (X*2).reshape(-1)

    if params.clf == 'rf':
        print('Using random forest')
        clf = RandomForestRegressor(n_estimators=int(params.num_of_trees))
    elif params.clf == 'svr':
        print('Using SVR')
        clf = SVR(C=float(params.svr_c))
    else:
        print('Using Linear Regression')
        clf = LinearRegression()

    clf.fit(X, y)

    predicted = clf.predict(X)

    if params.metric == 'mae':
        print('MAE:', mean_absolute_error(y, predicted))
    else:
        print('MSE:', mean_squared_error(y, predicted))










