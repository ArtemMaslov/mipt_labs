import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
import math as m
import random as r

from scipy.integrate import quad

mpl.rcParams['font.size'] = 14 # Управление стилем, в данном случаем - размером шрифта 

# Создаем фигуру
plt.figure(figsize=(16,9))

# Подписываем оси и график
plt.title(r"Распределение интенсивности")
plt.xlabel(r"x, м")
plt.ylabel("Отношение интенсивности в точки наблюдения к падающей $\\frac{I}{I_0}$")

# Добавляем данные
x = np.linspace(-0.25, 0.25, 40000) # м
wave_length =578e-9 # м
k = 2*m.pi/wave_length

d1 = 400e-6 # м
d2 = 300e-6 # м
D  = 1500e-6 # м
A0 = 1

z = 100 # м

def Intesive(xi, x):
    return m.cos(k / (2 * z) * (x - xi)**2)
    
def IntesiveSin(xi, x):
    return m.sin(k / (2 * z) * (x - xi)**2)

y = []

xi_1 = -d1 - D/2
xi_2 = D / 2

for _x in x:
    I1 = quad(Intesive, xi_1, xi_1 + d1, args = (_x))[0] + 1j * quad(IntesiveSin, xi_1, xi_1 + d1, args = (_x))[0]
    I2 = quad(Intesive, xi_2, xi_2 + d2, args = (_x))[0] + 1j * quad(IntesiveSin, xi_2, xi_2 + d2, args = (_x))[0]

    I = abs(I1 + I2)**2

    y.append(I)

y = np.array(y)

plt.plot(x, y, '.', color = 'k', markersize = 1)

# Активируем сетку
ax = plt.subplot()
ax.minorticks_on()

#  Определяем внешний вид линий основной сетки:
ax.grid(which = 'major', color = 'k', linewidth = 1)

#  Определяем внешний вид линий вспомогательной
#  сетки:
ax.grid(which = 'minor', color = 'k', linestyle = ':')

plt.grid(visible = True, which = 'major', axis = 'both', alpha = 0.7)
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.4)

# Активируем легенду графика
#plt.legend()

# Сохраняем изображение в текущую директорию
plt.savefig('Int_I.png')

# Внимание, запускаете вашу программу как сценарий, то что бы показать график
# Используйте эту команду
plt.show()