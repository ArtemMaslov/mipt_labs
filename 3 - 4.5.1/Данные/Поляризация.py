import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math as m
mpl.rcParams['font.size'] = 16 # Управление стилем, в данном случаем - размером шрифта 

# Создаем фигуру
plt.figure(figsize=(16,9))

# Подписываем оси и график
plt.title(r"Зависимость интенсивности лазерного излучения от угла поляроида")
plt.xlabel(r"Квадрат синуса угла поляризации")
plt.ylabel(r"Выходное напряжение в мВ")

# Добавляем данные

x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
y = np.array([1.9, 2.1, 2.7, 4.5, 6.1, 8.0, 9.0, 13.5, 16.0, 16.1])

x = (np.sin(x * m.pi/180)) ** 2

yerr = [0.2, 0.2, 0.2, 0.2, 0.6, 0.6, 1.0, 1.1, 1.0, 2.4]

plt.plot(x, y, '.', color = 'r')
#'r^' - задает стиль линии - красные (red) треугольники (^), подробнее в документации

# Данные с ошибками
#mu = np.sin(x2)
#sigma = np.abs(mu)**0.5
#y2 = np.random.normal(mu, sigma)
# Можно рисовать ошибки
plt.errorbar(x, y, yerr = yerr, fmt = '+', color = 'r')

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


# Сохраняем изображение в текущую директорию
plt.savefig('intense.png')

# Внимание, запускаете вашу программу как сценарий, то что бы показать график
# Используйте эту команду
plt.show()

