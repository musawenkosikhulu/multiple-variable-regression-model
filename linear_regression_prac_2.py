# -*- coding: utf-8 -*-
"""Linear_Regression_Prac_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17xMIzRimWyYhJmmGi6Vl6eHnSpAlJInK

## Linear Regression Prac 2

This notebook will make use of Scikit-learn's Linear Regression class. The documentation is found here: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

Credits:

The notebooks on linear regression are modifications of various sources which include:
https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
https://medium.com/analytics-vidhya/linear-regression-using-python-ce21aa90ade6
https://www.kdnuggets.com/2019/03/beginners-guide-linear-regression-python-scikit-learn.html/2

## Various Python imports
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

"""## Load the dataset"""

diabetes = datasets.load_diabetes()

"""## Take a look at what has been downloaded"""

diabetes

"""## Print out the feature names"""

diabetes['feature_names']

"""## Take a look at the shape of the data"""

diabetes['data'].shape

"""## Take a look at the shape of the targets (what we are predicting for)"""

diabetes['target'].shape

"""## Use all training features

In this notebook we are interested in creating a multiple variable regression model. So in this case, we will use all variables.

Typically, features are denoted as X and targets as Y (some authors will use 'y' instead).
"""

X = diabetes.data
y = diabetes['target']

"""## Check the shape!"""

X.shape

y.shape

"""## Split the data into training and testing sets"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4278) # 70% training and 30% test

"""## Check the training features shape"""

X_train.shape

"""## Check the testing features shape"""

X_test.shape

"""## Define a linear regression model"""

model = LinearRegression()

"""## Look at what has just being initialised"""

model

"""## Train the model/fit the model"""

model.fit(X_train, y_train)

"""## Print the coefficients"""

model.coef_

"""## Print the intercept"""

model.intercept_

"""## Task: can you write out the model given the above outputs?
y = 152 -48d1 -208d2 + 538d3 + 317d4 -412d5 +192d6 -7d7 + 210d8 + 608d9 + 49d10
...

## Apply the model to the testing features and get the predictions
"""

Y_pred = model.predict(X_test)

"""## Determine the performance of the model on the testing data

There are various options, but commonly used one include:

* mean squared error
* mean absolute error
* root mean squared error

There can be implemented using scikit-learn.

### Mean squared error
"""

mean_squared_error(y_test, Y_pred)

"""### Mean absolute error"""

mean_absolute_error(y_test, Y_pred)

"""### Root mean squared error"""

np.sqrt(mean_squared_error(y_test, Y_pred))

"""## Task: is the performance better than using a single variable?

Yes
"""