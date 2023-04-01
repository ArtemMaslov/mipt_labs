import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math as m
mpl.rcParams['font.size'] = 16 # Управление стилем, в данном случаем - размером шрифта 

# Создаем фигуру
plt.figure(figsize=(16,9))

# Подписываем оси и график
plt.title(r"Зависимость относительной интенсивности излучения от угла поляризации")
plt.xlabel(r"Угол поляризации")
plt.ylabel(r"Напряжение на фотодиоде")

# Добавляем данные

x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
y = (np.array([1.9, 2.1, 2.7, 4.5, 6.1, 8.0, 9.0, 13.5, 16.0, 16.1])- 1.9)/12.2

x1= np.linspace(0, 90, 10000)
y1 = np.sin(x1*m.pi/180)**2


yerr = np.array([0.2, 0.2, 0.2, 0.2, 0.6, 0.6, 1.0, 1.1, 1.0, 2.4])/12.2

plt.plot(x, y, '.', color = 'r', label = 'Эксперимент')
plt.plot(x1, y1, color = 'b', label = 'Теория')
#'r^' - задает стиль линии - красные (red) треугольники (^), подробнее в документации

# Данные с ошибками
#mu = np.sin(x2)
#sigma = np.abs(mu)**0.5
#y2 = np.random.normal(mu, sigma)
# Можно рисовать ошибки
plt.errorbar(x, y, xerr = 1, yerr = yerr, fmt = '+', color = 'r')

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
plt.legend(loc = 4)
plt.show()

