import numpy as np
from mysimplelinearregressor import MySimpleLinearRegressor as LR
from tabulate import tabulate
def main():
    # starting with PA4, we are goign to be implementing
    # ML algs using a standard API (application programming interface)
    # modeled after common ML libraries (sci-ki learn, tensorflow,...)

    # data convention
    # X: feature matrix (2D list AKA table where cols are features/attributes)
    # the class attribute is stored seperately in y
    # y: target vector/class vector (1D list of the values you want to predict)
    # X and y are parellel (same length and corresponding indexes)

    # we build a machine learning algorithm/model using "training data"
    # and evaluate a machine learning alg/model using "testing data"
    # split X and y
    # X_train and y_train (are parallel)
    # X_test and y_test (are parallel)

    # we will implement algs as classes
    # alg convention
    # each class will implement a common public API
    # with two methods
    # fit(X_train,y_train) -> None
    # "fits" the model (aka trains the alg) using training data
    # predict(X_test) -> y_predicted (list)
    # makes predictions for unseen instances in training data
    # y_predicted and y_test are parallel
    # we can determine how "good" the model alg is
    # by comparing these two lists
    # regression: numerical data
    # - MAE (Mean Absolute Error): avg of absolute values of the differences
    # between each pair in y_predicted and y_test
    # classification: categorical data
    # - accuracy: num of matching pairs in y_predicted and y_test/num of instances in the test

    #

    # we need training data
    np.random.seed(0)
    X_train= [[value] for value in range(100)]
    y_train = [row[0]*2 + np.random.normal(0,25) for row in X_train]

    my_lr = LR()
    my_lr.fit(X_train,y_train) # fits m and b to the training data
    X_test = [[150],[200], [900],[24]]
    y_predicted = my_lr.predict(X_test)
    print(y_predicted)

    # now, lets rework this example into unit testing form 
     



if __name__ == "__main__":
    main()
