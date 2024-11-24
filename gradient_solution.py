import numpy as np
from matplotlib import pyplot as plt

from computeCost import compute_cost
from saveTheta import saveThetaToFile
from utils import predict

def gradient_descent(X, y, learning_rate, epochs):

    m, n = X.shape

    X = np.c_[np.ones((m, 1)), X]  # Добавляем столбец единиц для свободного члена
    theta = np.zeros(n + 1)  # Инициализируем параметры
    history = []

    for _ in range(epochs):
        predictions = predict(X, theta)
        errors = predictions - y
        gradient = (1 / m) * X.T.dot(errors)
        if np.any(np.abs(gradient) > 1e10):
            print("Градиенты слишком большие, остановка обучения.")
            break
        theta -= learning_rate * gradient
        history.append(compute_cost(X, y, theta))

    return theta, history


def gradient_predict(X, y, alphas, epochs):
    best_alpha = None
    min_cost = float('inf')
    best_theta = None
    best_cost_history = None

    for a in alphas:
        theta_gd, history = gradient_descent(X, y, a, epochs)
        final_cost = history[-1]
        if final_cost < min_cost:
            min_cost = final_cost
            best_alpha = a
            best_theta = theta_gd
            best_cost_history = history

    print(f'Лучший коэффициент обучения: {best_alpha}')
    print(f'Лучшие theta для модели: {best_theta}')

    # Сохраняем параметры theta в файл
    saveThetaToFile(best_theta, filename="data/theta.json")

    # Построение графика изменения функции стоимости
    plt.plot(best_cost_history)
    plt.title('История изменения функции стоимости (Градиентный спуск)')
    plt.xlabel('Итерация')
    plt.ylabel('Стоимость')
    plt.show()
