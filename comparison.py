import math
import sys

EPSILON = sys.float_info.epsilon

def float_equal(a, b, epsilon=EPSILON):
    """ Compares to floats with a given epsilon. Normally you should use the
    epsilon constant EPSILON in this module (default value).

    Test:
    >>> float_equal(0, 0)
    True
    >>> float_equal(0.0000, 0.0000)
    True
    >>> float_equal(1, 0)
    False
    >>> float_equal(0.0, 0.00001)
    False
    >>> float_equal(4.00001, 4.00001)
    True
    >>> float_equal(125352.00001, 125352.00001)
    True
    """

    # Shortcut, handles infinities.
    if a == b:
        return True
    else:
        diff = math.fabs(a - b)
        # One or both are zero.
        if a * b == 0:
            # Relative error is not meaningful here.
            return diff < (epsilon * epsilon)
        # Use relative error.
        else:
            abs_a = math.fabs(a)
            abs_b = math.fabs(b)
            return diff / (abs_a + abs_b) < epsilon

def string_is_float(string):
    """ Checks if a string is a float.

    Test: 
    >>> string_is_float('1')
    True
    >>> string_is_float('1427')
    True
    >>> string_is_float('-1')
    True
    >>> string_is_float('-1427')
    True
    >>> string_is_float('1.0')
    True
    >>> string_is_float('1337.536')
    True
    >>> string_is_float('-153.0563')
    True
    >>> string_is_float('abc')
    False
    >>> string_is_float('1a')
    False
    >>> string_is_float('1,31434')
    False
    >>> string_is_float('1.341a')
    False
    >>> string_is_float('1314.142.')
    False
    """
    try:
        float(string)
        return True
    except ValueError:
        return False

def string_is_int(string):
    """ Checks if a string is a integer.

    Test: 
    >>> string_is_int('1')
    True
    >>> string_is_int('1427')
    True
    >>> string_is_int('-1')
    True
    >>> string_is_int('-1427')
    True
    >>> string_is_int('1.0')
    False
    >>> string_is_int('-1.0')
    False
    >>> string_is_int('abc')
    False
    >>> string_is_int('1a')
    False
    """
    try:
        int(string)
        return True
    except ValueError:
        return False
        
if __name__ == '__main__':
    print('Executing doctest.')
    import doctest
    doctest.testmod()