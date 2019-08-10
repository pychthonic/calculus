import numpy
import matplotlib.pyplot

def graph(func1, func2, func3, func4, x_range):
    x = numpy.array(x_range)
    y1 = func1(x)
    y2 = func2(x)
    y3 = func3(x)
    y4 = func4(x)
    line1 = matplotlib.pyplot.plot(x, y1, label="(1/2)*x+2")
    line2 = matplotlib.pyplot.plot(x, y2, label="5-2*x")
    line3 = matplotlib.pyplot.plot(x, y3, label="4-(x**2)")
    line4 = matplotlib.pyplot.plot(x, y4, label="(x-3)**2")
    matplotlib.pyplot.legend()
    matplotlib.pyplot.ylim((-10,10))
    matplotlib.pyplot.grid(linewidth=1)
    matplotlib.pyplot.axvline(color='black')
    matplotlib.pyplot.axhline(color='black')
    matplotlib.pyplot.show()

def func1(x):
    return (1/2)*x+2
def func2(x):
    return 5-2*x
def func3(x):
    return 4-(x**2)
def func4(x):
    return (x-3)**2


if __name__ == '__main__':
    graph(func1, func2, func3, func4, numpy.arange(-10, 10, .1))
