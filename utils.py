import numpy as np

def predict(X, w):
    return np.dot(X, w)
# def mean_squared_error(y_true, y_pred):
#     return np.mean((y_true - y_pred) ** 2)
