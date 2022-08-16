# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 18:00:45 2022

@author: User
"""

import pandas as pd
import numpy as np

#%% ETL - получение и очистка данных
# получаем файл Xls
xls = pd.ExcelFile("https://video.ittensive.com/math-stat/demo13.xls")

#%% получаем первый лист из xls файла
sheet = xls.parse(0)

#%% предподготовка (очистка данных)
"""
1. Выбираем 3й столбец (Unnamed: 2)
2. Берем строки, начиная с 6 до 34
3. Сбрасываем индекс
4. Выбираем только нужный столбец
5. Преобразовываем серию данных (Мужчины) во фрейм
"""
data = pd.DataFrame({'Мужчины': sheet['Unnamed: 2'][6:34].reset_index()['Unnamed: 2']})

#%% Построениеи обучение модели
# Возьмем среднее значение как самую простую модель
model = float(data.mean())

#%% Вычисление точности модели
# Рассчитаем ошибку по тестовым данным
err = np.abs(data - model).mean()
print ('{0:.3}%'.format(float(100*err/model)))

#%% Применение модели
# Сравним численность мужского населения России в 2021 году с моделью
# 2021 г - 67,85 млн.
result = 67.85
print ('{0:.3}%'.format(100 * (result - model) / result))