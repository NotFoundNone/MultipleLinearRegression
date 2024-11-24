# import numpy as np
# import matplotlib.pyplot as plt
#
# # Данные
# data = np.array([
#     [2104, 3, 399900], [1600, 3, 329900], [2400, 3, 369000],
#     [1416, 2, 232000], [3000, 4, 539900], [1985, 4, 299900],
#     [1534, 3, 314900], [1427, 3, 198999], [1380, 3, 212000],
#     [1494, 3, 242500], [1940, 4, 239999], [2000, 3, 347000],
#     [1890, 3, 329999], [4478, 5, 699900], [1268, 3, 259900],
#     [2300, 4, 449900], [1320, 2, 299900], [1236, 3, 199900],
#     [2609, 4, 499998], [3031, 4, 599000], [1767, 3, 252900],
#     [1888, 2, 255000], [1604, 3, 242900], [1962, 4, 259900],
#     [3890, 3, 573900], [1100, 3, 249900], [1458, 3, 464500],
#     [2526, 3, 469000], [2200, 3, 475000], [2637, 3, 299900],
#     [1839, 2, 349900], [1000, 1, 169900], [2040, 4, 314900],
#     [3137, 3, 579900], [1811, 4, 285900], [1437, 3, 249900],
#     [1239, 3, 229900], [2132, 4, 345000], [4215, 4, 549000],
#     [2162, 4, 287000], [1664, 2, 368500], [2238, 3, 329900],
#     [2567, 4, 314000], [1200, 3, 299000], [852, 2, 179900],
#     [1852, 4, 299900], [1203, 3, 239500]
# ])
#
# # Разделение данных, нормализация и добавление идиниц в столбец
# # Разделение на X и y
# X = data[:, :-1]  # Признаки
# y = data[:, -1]   # Целевая переменная
# m = len(y)        # Количество примеров
#
# # Нормализация признаков
# mean_X = np.mean(X, axis=0)
# std_X = np.std(X, axis=0)
# X_norm = (X - mean_X) / std_X
#
# # Добавление столбца единиц к X
# X_aug = np.hstack([np.ones((m, 1)), X_norm])
#
# # Реализация функции стоимости
# def compute_cost(X, y, theta):
#     m = len(y)
#     predictions = X @ theta
#     cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
#     return cost
#
# # Градиентный спуск
# def gradient_descent(X, y, theta, alpha, num_iters):
#     m = len(y)
#     cost_history = []
#     for _ in range(num_iters):
#         theta -= (alpha / m) * (X.T @ (X @ theta - y))
#         cost_history.append(compute_cost(X, y, theta))
#     return theta, cost_history
#
# # Инициализация
# theta = np.zeros(X_aug.shape[1])
# alpha = 0.01
# num_iters = 1000
#
# # Подбор скорости обучения
# alphas = [0.0000001, 0.5]
# best_alpha = alphas[0]
# lowest_cost = float('inf')
#
# # Тут мы просто проходимся циклом по различным скоростям обучения для выбора оптимакльной
# for a in alphas:
#     temp_theta, temp_cost = gradient_descent(X_aug, y, np.zeros(X_aug.shape[1]), a, num_iters)
#     if temp_cost[-1] < lowest_cost:
#         lowest_cost = temp_cost[-1]
#         best_alpha = a
#
# print(best_alpha)
#
# # Градиентный спуск с лучшей скоростью
# theta_gd, cost_history = gradient_descent(X_aug, y, np.zeros(X_aug.shape[1]), best_alpha, num_iters)
#
# # Аналитическое решение
# theta_analytical = np.linalg.pinv(X_aug.T @ X_aug) @ X_aug.T @ y
#
# # Предсказания
# predictions_gd = X_aug @ theta_gd
# predictions_analytical = X_aug @ theta_analytical
#
# # Вычисление MSE
# mse_gd = np.mean((predictions_gd - y) ** 2)
# mse_analytical = np.mean((predictions_analytical - y) ** 2)
#
# # Вывод результатов
# print("Градиентный спуск:")
# print(f"Параметры: {theta_gd}")
# print(f"MSE: {mse_gd}")
#
# print("\nАналитическое решение:")
# print(f"Параметры: {theta_analytical}")
# print(f"MSE: {mse_analytical}")
#
# # График изменения стоимости
# plt.plot(range(len(cost_history)), cost_history, label="Градиентный спуск")
# plt.xlabel("Итерации")
# plt.ylabel("Стоимость J(θ)")
# plt.legend()
# plt.show()
