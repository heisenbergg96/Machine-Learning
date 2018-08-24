import numpy as np
import math
from CleanData import X
from CleanData import Y

from CleanData import theta
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn import linear_model

#function for calculating theta:featues
def gradient_descent(X, Y, theta, alpha, iterations):
    no_of_rows = len(Y)
    for iteration in range(iterations):
        h = X.dot(theta)
        error = h - Y
        gradient = X.T.dot(error)
        theta = theta - alpha * gradient/no_of_rows
    return theta

#splitting the dataset into test data and train data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)

#call gradient descent 
thetas = gradient_descent(X_train,Y_train,theta,0.000000001,100000)

#predicted values against test data		
pred = X_test.dot(thetas)

#mean absolute error 
print mean_absolute_error(Y_test,pred)

#using scikit learn's linear regression function
lm = linear_model.LinearRegression()
model = lm.fit(X_train,Y_train)
predictions = lm.predict(X_test)

#mean_absolute_error for scikit learn's model
print mean_absolute_error(Y_test,predictions)																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																				