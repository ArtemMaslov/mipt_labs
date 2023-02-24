import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math as m
import random as r

mpl.rcParams['font.size'] = 16 # Управление стилем, в данном случаем - размером шрифта 

# Создаем фигуру
plt.figure(figsize=(16,9))

# Подписываем оси и график
plt.title(r"Распределение интенсивности")
plt.xlabel(r"Theta(рад)")
plt.ylabel(r"$\abs{g}^2$")

# Добавляем данные
x = np.linspace(-1/400, 1/400, 50000)
l =578e-9
k = 2*m.pi/l
b1 = 4e-4
b2 = 3e-4
d = 15e-4

def f (x, b):
    return (np.sin(k*b/2 * np.sin(x)) / (k*b/2 * np.sin(x)))**2

y = (f(x,b1)*f(x,b1) + f(x,b2)*f(x,b2) + 2*f(x,b1)*f(x,b2)*np.cos(k*d*np.sin(x)))



plt.plot(x, y, '.', color = 'k')
#'r^' - задает стиль линии - красные (red) треугольники (^), подробнее в документации

# Данные с ошибками
#mu = np.sin(x2)
#sigma = np.abs(mu)**0.5
#y2 = np.random.normal(mu, sigma)
# Можно рисовать ошибки
#plt.errorbar(x, y, yerr = 0.01, fmt = '+', color = 'r')

# Активируем сетку
ax = plt.subplot()
ax.minorticks_on()

#  Определяем внешний вид линий основной сетки:
ax.grid(which = 'major', color = 'k', linewidth = 1)

#  Определяем внешний вид линий вспомогательной
#  сетки:
ax.grid(which = 'minor', color = 'k', linestyle = ':')

plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1)
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.75)

# Активируем легенду графика
#plt.legend()

# Сохраняем изображение в текущую директорию
plt.savefig('I.png')

# Внимание, запускаете вашу программу как сценарий, то что бы показать график
# Используйте эту команду
plt.show()

