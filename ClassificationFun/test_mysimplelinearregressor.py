import numpy as np
from mysimplelinearregressor import MySimpleLinearRegressor as LR
from sklearn.linear_model import LinearRegression

# test modules and test functions (AKA unit tests)
# with pytest start with test_

def test_mysimplelinearregressor_fit():

    np.random.seed(0)
    X_train= [[value] for value in range(100)]
    y_train = [row[0]*2 + np.random.normal(0,25) for row in X_train]
    my_lr = LR()
    my_lr.fit(X_train,y_train)

    # 2 main ways to write asserts
    # 1. againsts a desk calculation (hardcoded)
    slope_solution = 1.92491754843044
    intercept_solution = 5.211786196055144
    assert np.isclose(my_lr.slope, slope_solution)
    assert np.isclose(my_lr.intercept, intercept_solution)

    # 2. against a known correct implementation
    # lets assert against slope and intercept vals from
    # sci-kit learn's linear regression
    sklearn_lr = LinearRegression()
    sklearn_lr.fit(X_train,y_train)
    assert np.isclose(my_lr.slope, sklearn_lr.coef_[0])
    assert np.isclose(my_lr.intercept, sklearn_lr.intercept_)

def test_mysimplelinearregressor_predict():
    np.random.seed(0)
    X_train= [[value] for value in range(100)]
    y_train = [row[0]*2 + np.random.normal(0,25) for row in X_train]

    my_lr = LR()
    my_lr.fit(X_train,y_train) # fits m and b to the training data
    X_test = [[150],[200], [900],[24]]
    y_predicted = my_lr.predict(X_test)
    sklearn_lr = LinearRegression()
    sklearn_lr.fit(X_train,y_train)
    sklearn_y_predict = sklearn_lr.predict(X_test)
    assert np.allclose(y_predicted, sklearn_y_predict)


