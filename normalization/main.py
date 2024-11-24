import data_loader
import normalization
import visualization
from data_saver import save_normalized_data

file_path = "../data/ex1data2.txt"
# Load data
df = data_loader.load_data(file_path)

# Применение нормализации
df['GearCount_MinMax'] = normalization.min_max_normalize(df, 'GearCount')
df['GearCount_Standart'] = normalization.standart_normalize(df, 'GearCount')
df['GearCount_Max'] = normalization.max_normalize(df, 'GearCount')

df['EngineSpeedRPM_MinMax'] = normalization.min_max_normalize(df, 'EngineSpeedRPM')
df['EngineSpeedRPM_Standart'] = normalization.standart_normalize(df, 'EngineSpeedRPM')
df['EngineSpeedRPM_Max'] = normalization.max_normalize(df, 'EngineSpeedRPM')

df['Price_MinMax'] = normalization.min_max_normalize(df, 'Price')
df['Price_Standart'] = normalization.standart_normalize(df, 'Price')
df['Price_Max'] = normalization.max_normalize(df, 'Price')

#Средние значения признаков
mean = {
    'EngineSpeedRPM': normalization.compute_mean(df['EngineSpeedRPM']),
    'GearCount': normalization.compute_mean(df['GearCount']),
    'Price': normalization.compute_mean(df['Price'])
}

#Стандартные квадратичные отклонения признаков
std = {
    'EngineSpeedRPM': normalization.compute_std(df['EngineSpeedRPM']),
    'GearCount': normalization.compute_std(df['GearCount']),
    'Price': normalization.compute_std(df['Price'])
}

print("Средние значения признаков:")
print(mean)
print("\nСтандартные квадратичные отклонения признаков:")
print(std)

columns_to_save = ['GearCount_MinMax', 'EngineSpeedRPM_MinMax', 'Price_MinMax']

# Сохраняем нормализованные данные
save_normalized_data(df, columns_to_save, filename="../data/min_max_normalized_data.csv")

# Визуализация результатов
visualization.visualize_data(df)