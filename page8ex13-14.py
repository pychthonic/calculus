import numpy
import matplotlib.pyplot

"""Started working with masked values here, to keep matplotlib from connecting
the lines where they approach infinity in opposite directions. Also figured out
how to get Sublime to work with the virtualenv I have set up so I can use it
instead of IDLE which was driving me up the wall.
"""

def graph(func1, func2, x_range):
    x = numpy.array(x_range)

    y1 = func1(x)
    x1 = numpy.ma.masked_values(x, 0)
    matplotlib.pyplot.plot(x1, y1, label="y = 3/x")

    y2 = func2(x)
    x2 = numpy.ma.masked_values(x, -2)
    matplotlib.pyplot.plot(x2, y2, label="y = 1/(x+2)")

    matplotlib.pyplot.legend()
    matplotlib.pyplot.ylim((-10,10))
    matplotlib.pyplot.grid(linewidth=1)
    matplotlib.pyplot.axvline(color='black')
    matplotlib.pyplot.axhline(color='black')
    matplotlib.pyplot.show()

def func1(x):
    return 3/x
def func2(x):
    return 1/(x+2)


if __name__ == '__main__':
    graph(func1, func2, numpy.arange(-10, 10, .1))