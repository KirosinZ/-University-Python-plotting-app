from math import radians
import numpy as np
import matplotlib.pyplot as plt

def SinAndLog(start, end, step):
    figure = plt.gcf()
    figure.patch.set_facecolor((0.3, 0.8, 1))
    figure.canvas.manager.set_window_title('1. Синус и натуральный логарифм')

    x = np.arange(start, end, step)

    sin = np.sin(x)
    log = np.log(x)

    plt.plot(x, sin, color = (0.2, 0.8, 1))
    plt.plot(x, log, color = (1, 0.6, 0))
    plt.show()

def OverlappingCircles(x1, y1, r1, x2, y2, r2):
    figure = plt.gcf()
    figure.patch.set_facecolor((0.3, 0.8, 1))
    figure.canvas.manager.set_window_title('2. Пересекающиеся окружности')

    px = 1 / plt.rcParams['figure.dpi']
    figure.set_size_inches(500 * px, 500 * px)

    phi = np.arange(0, radians(360), radians(0.01))

    x = np.cos(phi)
    y = np.sin(phi)

    plt.plot(r1 * x + x1, r1 * y + y1, color = (1, 0, 0.4), linewidth = 2, linestyle = '-.')
    plt.plot(r2 * x + x2, r2 * y + y2, color = (0, 0, 1), linewidth = 3, linestyle = '--')
    plt.gca().set_facecolor((1, 0.8, 1))

    plt.show()

def TwoGraphs():
    figure = plt.gcf()
    figure.patch.set_facecolor((0.3, 0.8, 1))
    figure.canvas.manager.set_window_title('3. Два графика')

    px = 1 / plt.rcParams['figure.dpi']
    figure.set_size_inches(1150*px,500*px)

    t = np.arange(-radians(3600), radians(3600), radians(0.01))

    x = -0.35 * np.cos(t) + np.cos(-0.35 * t)
    y = -0.35 * np.sin(t) - np.sin(-0.35 * t)

    plt.subplot(1,2,1)
    plt.title('Спирограф')
    plt.plot(x,y, color = (0, 1, 0), linewidth = 2)

    phi = np.arange(0, radians(3600), radians(0.01))

    plt.subplot(1,2,2, projection = 'polar')
    plt.title('Золотая спираль')
    plt.plot(phi, np.exp(2 * phi / np.pi) / np.exp((np.sqrt(5) + 1) / 2), color = (0.8, 0.6, 0), linewidth = 3, linestyle = ':')

    plt.show()

def main():
    #SinAndLog(0, 10, 0.01)
    #OverlappingCircles(-2,-3,6, 4, 11, 14)
    TwoGraphs()

main()