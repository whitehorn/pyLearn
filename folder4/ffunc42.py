
# ЛИСТИНГ "А" Пакеты main1

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:48:27 2016

@author: pasha
"""

import sys
import math
import random
import numpy as np

def haversine(origin, destination):
    '''
    Points are tuples of (latitude, longitude)
    '''
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371. # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2.) * math.sin(dlat/2.) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2.) * math.sin(dlon/2.)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1.-a))
    d = radius * c

    return d

def pirson_cc(x, y):
    u'''
    Это строка документирования!
    Функция вычисляет для двух последовательностей \
    коэффициент корреляции Пирсона.
    
    Входящие параметры:
    ===================
    
    **x [ndarray]** - одномерный массив длины N;
    **y [ndarray]** - одномерный массив длины N;
    
    Результат выполнения функции:
    =============================
    **сс [float]** - коэффициент корреляции Пирсона.
    '''
    
    xm = x.mean()
    ym = y.mean()

    a = 0
    b1 = 0
    b2 = 0
    for xi, yi in zip(x, y):
        a += (xi - xm)*(yi - ym)
        b1 += (xi - xm)**2 
        b2 += (yi - ym)**2
    b = np.sqrt(b1*b2)
    
    cc = float(a)/b
    return cc

# **************************************

if __name__ == 'main':
    N = 60
    # методы списка + модуль random
    a = list(range(N))
    random.shuffle(a)
    a = np.array(a)
    
    # модуль numpy
    b = np.arange(N)
    np.random.shuffle(b)
    
    TSK = (56.49, 84.95)   # 56°29′19″ с. ш. 84°57′08″ в. д.
    MSK = (55.76, 37.61)  # 55°45′21″ с. ш. 37°37′04″ в. д.
    SPB = (59.95, 30.61) # 59°57′00″ с. ш. 30°19′00″ в. д. (G) (O) (Я)
    
    filename = sys.argv
    print((f'Привет! Я файл {filename[0]} и ты видишь это всё,'
           'хотя хотел импортировать лишь одну функцию haversine'))
    print ('От Москвы до Ленинграда {:.2f} км'.format(haversine(SPB, MSK)))
    print ('CC from def cc: {:.3f}'.format(pirson_cc(a, b)))
    print ('\n Сравни: \n')
    print ('CC from numpy: {:.3f}'.format(np.corrcoef(a, b)[0][1]))