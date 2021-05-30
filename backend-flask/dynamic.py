import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error as mse
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts


def train_testing(x, y):
    x_train, x_test, y_train, y_test = tts(x, y, random_state=0, test_size=3/10)
    regr = LinearRegression()
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)
    return regr.intercept_, regr.coef_, r2_score(y_pred, y_test), np.sqrt(mse(y_pred, y_test))


def train_testing_pred(x_train, x_test, y_train, y_test):
    regr = LinearRegression()
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)
    return regr.intercept_, regr.coef_, r2_score(y_pred, y_test), np.sqrt(mse(y_pred, y_test))

def set_variables(items):
    ## do something for checking the shit
    return True