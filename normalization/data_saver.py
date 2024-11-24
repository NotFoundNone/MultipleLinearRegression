import pandas as pd


def save_normalized_data(df, columns, filename="../data/normalized_data.csv"):

    try:
        # Фильтруем только необходимые колонки
        normalized_data = df[columns]
        # Сохраняем в файл
        normalized_data.to_csv(filename, index=False)
        print(f"Нормализованные данные успешно сохранены в файл: {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")
