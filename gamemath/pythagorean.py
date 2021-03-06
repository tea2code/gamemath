﻿import math

def euclidean_distance( x1, y1, x2, y2 ):
    """ Calculates the euclidean distance between two points in second dimension.

    Test:
    >>> print('{0:.4f}'.format(euclidean_distance(2, -1, -2, 2)))
    5.0000
    """
    a = x1 - x2
    b = y1 - y2
    return solve_c(a, b)

def point_line_distance( x1, y1, x2, y2, x3, y3 ):
    """ Calculates distance between a point (x1, y1) and a line defined by (x2, y2) and (x3, y3). 
    
    Test:
    >>> print('{0:.2f}'.format(point_line_distance(1, 0, 0, -1, 0, 1)))
    1.00
    """
    normal_length = euclidean_distance( x2, y2, x3, y3 )
    return math.fabs((x1 - x2) * (y3 - y2) - (y1 - y2) * (x3 - x2)) / normal_length
    
def solve_c( a, b ):
    """ Calculates c of the pythagorean theorem: c² = a² + b² 
    
    Test:
    >>> print('{0:.2f}'.format(solve_c(2, 5)))
    5.39
    >>> print('{0:.2f}'.format(solve_c(45.563, 131.34)))
    139.02
    """
    return math.sqrt((a * a) + (b * b))
        
if __name__ == '__main__':
    print('Executing doctest.')
    import doctest
    doctest.testmod()