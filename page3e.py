import numpy
import matplotlib.pyplot

def graph(formula, x_range):
    x = numpy.array(x_range)
    y = formula(x)
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.ylim((-10000,10000))
    matplotlib.pyplot.grid(linewidth=1, markevery=2)
    matplotlib.pyplot.axvline(color='black', label="y-axis")
    matplotlib.pyplot.axhline(color='black')
    matplotlib.pyplot.show()

def my_formula(x):
    return -((x+12)**3)

if __name__ == '__main__':
    graph(my_formula, numpy.arange(-40, 10, .1))
