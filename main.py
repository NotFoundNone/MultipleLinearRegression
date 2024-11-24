from gradient_solution import gradient_predict
from analytical_solution import analytical_solution
from data_loader import load_data

# Загрузка данных
file_path = 'data/ex1data2.txt'
X, y = load_data(file_path)

# Градиентный спуск
alphas = [0.0000001, 0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 0.8, 1.1, 1.2, 1.3, 1.4, 1.5]
epochs = 10000

gradient_predict(X, y, alphas, epochs)

# # Аналитическое решение
theta_analytical = analytical_solution(X, y)


# # Сравнение предсказаний
# y_pred_gd = predict(X, theta_gd)
# y_pred_analytical = predict(X, theta_analytical)
# #
# # Оценка качества
# mse_gd = mean_squared_error(y, y_pred_gd)
# mse_analytical = mean_squared_error(y, y_pred_analytical)
#
# print("Параметры, найденные методом градиентного спуска:", theta_gd)
# print("Параметры, найденные аналитическим методом:", theta_analytical)
#
# print("\nСреднеквадратичная ошибка (Градиентный спуск):", mse_gd)
# print("Среднеквадратичная ошибка (Аналитический метод):", mse_analytical)