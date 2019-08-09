import numpy
import matplotlib.pyplot

def graph(formula, x_range):
    x = numpy.array(x_range)
    y = formula(x)
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.ylim((-1000,1000))
    matplotlib.pyplot.grid(linewidth=1)
    matplotlib.pyplot.axvline(color='black', label="y-axis")
    matplotlib.pyplot.axhline(color='black')
    matplotlib.pyplot.show()

def my_formula(x):
    return 3*(x**3)-(40*(x**2))+(50*x)-45

if __name__ == '__main__':
    graph(my_formula, numpy.arange(-20, 20, .1))
