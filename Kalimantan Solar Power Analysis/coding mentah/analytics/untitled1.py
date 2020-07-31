# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:19:35 2019

@author: YOSIA AZARYA
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataku=pd.read_csv("dataku.csv", sep=';')
dataku.head()

Temp = dataku['Temp']
RH = dataku['RH']
Eff = dataku['Eff']
Output = dataku['Output']
SA = dataku['SA']

angka = np.arange(0,1399)

plt.figure()
plt.scatter(angka, Temp)
plt.title("Sebaran nilai Temperature")
plt.ylabel("Temperature")
plt.show()

plt.figure()
plt.scatter(angka, RH)
plt.title("Sebaran nilai Kelembaban Relatif")
plt.ylabel("Kelembaban Relatif")
plt.show()

plt.figure()
plt.scatter(angka, SA)
plt.title("Sebaran nilai Radiasi Matahari")
plt.ylabel("Radiasi Matahari")
plt.show()

dataku.sort_values(by='Temp', ascending=True)
plt.figure()
plt.scatter(Temp, Eff)
plt.xlabel("Temperature")
plt.ylabel("Effisiensi Solar Panel")
plt.show()

dataku.sort_values(by='RH', ascending=True)

plt.figure()
plt.scatter(RH, Eff)
plt.xlabel("Kelembaban Relatif")
plt.ylabel("Effisiensi Solar Panel")
plt.show()