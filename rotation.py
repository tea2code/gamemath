import math

def rotate_x(x, y, angle, degree=True):
    """ Rotates the x-component of a coordinate using the angle (default in degree).
    Positive direction is counter clock wise.

    Test:
    >>> print('{0:.2f}'.format(rotate_x(0, 1, 90)))
    -1.00
    >>> print('{0:.2f}'.format(rotate_x(0, 1, 180)))
    -0.00
    >>> print('{0:.2f}'.format(rotate_x(0, 1, math.radians(90), False)))
    -1.00
    >>> print('{0:.2f}'.format(rotate_x(0, 1, math.radians(180), False)))
    -0.00
    """
    angle_radian = math.radians(angle) if degree else angle
    return x * math.cos(angle_radian) - y * math.sin(angle_radian)
    
def rotate_y(x, y, angle, degree=True):
    """ Rotates the y-component of a coordinate using the angle (default in degree).
    Positive direction is counter clock wise.

    Test:
    >>> print('{0:.2f}'.format(rotate_y(0, 1, 90)))
    0.00
    >>> print('{0:.2f}'.format(rotate_y(0, 1, 180)))
    -1.00
    >>> print('{0:.2f}'.format(rotate_y(0, 1, math.radians(90), False)))
    0.00
    >>> print('{0:.2f}'.format(rotate_y(0, 1, math.radians(180), False)))
    -1.00
    """
    angle_radian = math.radians(angle) if degree else angle
    return y * math.cos(angle_radian) + x * math.sin(angle_radian)
    
if __name__ == '__main__':
    print('Executing doctest.')
    import doctest
    doctest.testmod()