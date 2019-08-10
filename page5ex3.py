import numpy, sympy

def test_for_symmetry(func):
    test_numbers = numpy.arange(-1000000,1000000)
    symmetry_dict = {'y_symmetry': True, 'origin_symmetry': True}
    for x in test_numbers:
        if func(x) != func(-x):
            symmetry_dict['y_symmetry'] = False
            print('Function does not appear symmetric with respect to the y-axis.')
            break
    if symmetry_dict['y_symmetry']:
        print('Function appears symmetric with respect to the y-axis.')
    
    for x in test_numbers:
        if func(-x) != -func(x):
            symmetry_dict['origin_symmetry'] = False
            print("Function does not appear symmetric with respect to the origin.")
            break
    if symmetry_dict['origin_symmetry'] == True:
        print("Function appears to be symmetric with respect to the origin.")
        
    return symmetry_dict

if __name__ == '__main__':
    def func(x):
        return (x**2)-3
    symmetry_dict = test_for_symmetry(func)
