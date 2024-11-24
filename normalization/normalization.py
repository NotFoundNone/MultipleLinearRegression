
# Вычисление среднего значения
def compute_mean(data):
    return sum(data) / len(data)

# Вычисление среднеквадратичного отклонения
def compute_std(data):
    mean = compute_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5

# Min-Max нормировка
def min_max_normalize(df, column):
    min_val = min(df[column])  # Минимальное значение
    max_val = max(df[column])  # Максимальное значение
    return [(x - min_val) / (max_val - min_val) for x in df[column]]

# Стандартизация
def standart_normalize(df, column):
    data = df[column]
    mean = compute_mean(data)  # Среднее значение по определению
    std = compute_std(data)    # Стандартное отклонение по определению
    return [(x - mean) / std for x in data]

def max_normalize(df, column):
    data = df[column]
    max_val = max(df[column])
    return data / max_val
