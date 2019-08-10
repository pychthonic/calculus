import numpy, sympy

def find_points_of_intersection(func1, func2):
    test_numbers = numpy.arange(-1000,1000)
    intersecting_coordinate_list = []
    for x in test_numbers:
        if func1(x) == func2(x):
            intersecting_coordinate_list.append((x, func1(x)))
            print(f"Found intersecting coordinates: {intersecting_coordinate_list[-1]}")
    return intersecting_coordinate_list

if __name__ == '__main__':
    def func1(x):
        return (x - 1)
    def func2(x):
        return ((x**2) - 3)
    points_of_intersection = find_points_of_intersection(func1, func2)
