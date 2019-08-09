import numpy
import matplotlib.pyplot

def graph(formula, x_range):
    x = numpy.array(x_range)
    y = formula(x)
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.ylim((-50,75))
    matplotlib.pyplot.grid(linewidth=1, markevery=2)
    matplotlib.pyplot.axvline(color='black', label="y-axis")
    matplotlib.pyplot.axhline(color='black')
    matplotlib.pyplot.show()

def my_formula(x):
    return (x**3) - (3*(x**2)) + (2*x) + 25

if __name__ == '__main__':
    graph(my_formula, numpy.arange(-6.0, 6.0, .1))
