import numpy
import matplotlib.pyplot

def graph(func1, func2, func3, func4, x_range):
    x = numpy.array(x_range)
    y1 = func1(x)
    x_func2 = x
    x_func2_indexes_to_delete = []
    for i in range(len(x)):
        if ((9 - (x[i]**2)) < 0 ):
            x_func2_indexes_to_delete.append(i)
    for i in sorted(x_func2_indexes_to_delete, reverse=True):
        x_func2 = numpy.delete(x_func2, i)
    y2 = func2(x_func2)
    y3 = func3(x)
    y4 = func4(x)
    matplotlib.pyplot.plot(x, y1)
    matplotlib.pyplot.plot(x_func2, y2)
    matplotlib.pyplot.plot(x, y3)
    matplotlib.pyplot.plot(x, y4)
    matplotlib.pyplot.ylim((-10,10))
    matplotlib.pyplot.grid(linewidth=1)
    matplotlib.pyplot.axvline(color='black')
    matplotlib.pyplot.axhline(color='black')
    matplotlib.pyplot.show()

def func1(x):
    return (-3/2)*x+3
def func2(x):
    return numpy.sqrt(9-(x**2))
def func3(x):
    return 3 - (x**2)
def func4(x):
    return (x**3)-x


if __name__ == '__main__':
    graph(func1, func2, func3, func4, numpy.arange(-10, 10, .0001))
