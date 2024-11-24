import pandas as pd

def load_data(file_path):

    data = pd.read_csv(file_path)
    X = data.iloc[:, :-1].values  # Признаки: все столбцы, кроме последнего
    y = data.iloc[:, -1].values   # Целевая переменная: последний столбец
    return X, y
