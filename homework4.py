import numpy as np

def pearson_correlation(x, y):
    # Проверка на совпадение длин массивов
    if len(x) != len(y):
        raise ValueError("Массивы должны быть одинаковой длины")

    # Средние значения для x и y
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Вычисление числителя и знаменателя для формулы корреляции Пирсона
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator_x = sum((xi - mean_x) ** 2 for xi in x)
    denominator_y = sum((yi - mean_y) ** 2 for yi in y)

    # Вычисление корреляции Пирсона
    correlation = numerator / (np.sqrt(denominator_x) * np.sqrt(denominator_y))

    return correlation

# Пример использования
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]

print("Корреляция Пирсона между массивом 1 и массивом 2:", pearson_correlation(array1, array2))
