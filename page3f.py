import numpy
import matplotlib.pyplot

def graph(formula, x_range):
    x = numpy.array(x_range)
    y = formula(x)
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.ylim((-100000,100000))
    matplotlib.pyplot.grid(linewidth=1)
    matplotlib.pyplot.axvline(color='black')
    matplotlib.pyplot.axhline(color='black')
    matplotlib.pyplot.show()

def my_formula(x):
    return (x-2)*(x-4)*(x-6)

if __name__ == '__main__':
    graph(my_formula, numpy.arange(-60, 60, .1))
