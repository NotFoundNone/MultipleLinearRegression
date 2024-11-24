import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, header=None)  # Загружаем файл без заголовков
    df.columns = ['EngineSpeedRPM', 'GearCount', 'Price']  # Присваиваем имена столбцам
    return df