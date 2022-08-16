# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:21:15 2022

@author: User
"""
#%%
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams
rcParams ['figure.figsize'] = 16, 8

#%% получаем данные из csv файлов
data = pd.read_csv("http://video.ittensive.com/machine-learning/ashrae/train.0.0.csv.gz")
print (data.head())

#%% Визуализация данных. 
# Построим зависимость ТОЕ от даты/времени
data.set_index('timestamp')['meter_reading'].plot()
plt.show()

#%% Построение простой модели
# Возьмем среднее
model = float(data['meter_reading'].mean())
print ('{0:.4}'.format(model)) # результат 146,5

#%% Вычисление точности модели 
# Рассчитаем ошибку по данным
err = np.abs(data['meter_reading'] - model).mean()
print ('{0:.3}%'.format(float(100*err/model)))
# результат 78,3% (плохая точность - большое значение ошибки)

