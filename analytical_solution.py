import numpy as np

from saveTheta import saveThetaToFile


def analytical_solution(X, y):

    X = np.c_[np.ones((X.shape[0], 1)), X]  # Добавляем столбец единиц для свободного члена

    #Транспонируем матрицу
    X_T = X.T

    # theta = (X^T * X)^(-1) * X^T * y
    theta = np.linalg.inv(X_T.dot(X)).dot(X_T).dot(y)

    print(f'theta для модели: {theta}')

    saveThetaToFile(theta, filename="data/analytical_theta.json")
