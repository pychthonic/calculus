import numpy

def find_x_intercept(func):
    x_intercepts = []
    for x in numpy.arange(-1000.0, 1000.0, .5):
        if func(x) == 0:
            x_intercepts.append(x)
    return x_intercepts

if __name__ == '__main__':
    def func(x):
        return (x**3)-(4*x)
    x_intercepts = find_x_intercept(func)
    x_intercepts = [(x_intercept, 0) for x_intercept in x_intercepts]
    print(f"X-intercepts are {', '.join(map(str,x_intercepts))}")
