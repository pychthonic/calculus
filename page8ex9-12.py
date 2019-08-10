import numpy
import matplotlib.pyplot

def graph(func1, func2, func3, func4, x_range):
    x = numpy.array(x_range)
    y1 = func1(x)
    y2 = func2(x)
    
    x_func3 = x
    x_func3_indexes_to_delete = []
    for i in range(len(x)):
        if x[i] < 0:
            x_func3_indexes_to_delete.append(i)
    for i in sorted(x_func3_indexes_to_delete, reverse=True):
        x_func3 = numpy.delete(x_func3, i)
    y3 = func3(x_func3)
    
    x_func4 = x
    x_func4_indexes_to_delete = []
    for i in range(len(x)):
        if (x[i]+2) < 0:
            x_func4_indexes_to_delete.append(i)
    for i in sorted(x_func4_indexes_to_delete, reverse=True):
        x_func4 = numpy.delete(x_func4, i)
    y4 = func4(x_func4)
    matplotlib.pyplot.plot(x, y1, label="abs(x+2)")
    matplotlib.pyplot.plot(x, y2, label="abs(x)-1")
    matplotlib.pyplot.plot(x_func3, y3, label="numpy.sqrt(x)-6")
    matplotlib.pyplot.plot(x_func4, y4, label="numpy.sqrt(x+2)")
    matplotlib.pyplot.legend()
    matplotlib.pyplot.ylim((-10,10))
    matplotlib.pyplot.grid(linewidth=1)
    matplotlib.pyplot.axvline(color='black')
    matplotlib.pyplot.axhline(color='black')
    matplotlib.pyplot.show()

def func1(x):
    return abs(x+2)
def func2(x):
    return abs(x)-1
def func3(x):
    return numpy.sqrt(x)-6
def func4(x):
    return numpy.sqrt(x+2)


if __name__ == '__main__':
    graph(func1, func2, func3, func4, numpy.arange(-10, 10, .01))
