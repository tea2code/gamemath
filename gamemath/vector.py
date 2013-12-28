from . import comparison, pythagorean

class Vector2:
    """ A 2D vector.

    Member:
    x -- The x component (float).
    y -- The y component (float).
    """

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def clone(self):
        """ Creates a copy of this vector with same x and y.

        Test:
        >>> v = Vector2(1, 2)
        >>> c = v.clone()
        >>> v is c
        False
        >>> v == c
        True
        """
        return self.__copy__()

    def length(self):
        """ Calculates the length of a vector.

        Test:
        >>> print('{0:.3f}'.format(Vector2(1, 1).length()))
        1.414
        >>> print('{0:.3f}'.format(Vector2(45, 127).length()))
        134.737
        >>> print('{0:.3f}'.format(Vector2(5, 3).length()))
        5.831
        >>> print('{0:.3f}'.format(Vector2(-1, 1).length()))
        1.414
        >>> print('{0:.3f}'.format(Vector2(45, -127).length()))
        134.737
        >>> print('{0:.3f}'.format(Vector2(-5, -3).length()))
        5.831
        """
        return pythagorean.solve_c(self.x, self.y)

    def tuple(self):
        """ Returns a tuple representation of this vector.

        Test:
        >>> v = Vector2(1, 2)
        >>> v.tuple()
        (1, 2)
        """
        return self.x, self.y

    def __add__(self, other):
        """ Add two vectors using + operator. Returns the resulting vector.

        Test:
        >>> v1 = Vector2(1, 2)
        >>> v2 = Vector2(3, 4)
        >>> v3 = v1 + v2
        >>> v3.x
        4
        >>> v3.y
        6
        """
        return Vector2(self.x + other.x, self.y + other.y)

    def __copy__(self):
        """ Used when copy.copy() is called on a vector.

        Test:
        >>> import copy
        >>> v = Vector2(1, 2)
        >>> c = copy.copy(v)
        >>> v is c
        False
        >>> v == c
        True
        """
        return Vector2(self.x, self.y)

    def __eq__(self, other):
        """ Equality using the == operator.

        Test:
        >>> v1 = Vector2(1.0001, 21.0001)
        >>> v2 = Vector2(1.0001, 21.0001)
        >>> v3 = Vector2(1.0001, 21.000100001)
        >>> v1 == v2
        True
        >>> v1 == v3
        False
        """
        return comparison.float_equal(self.x, other.x) and \
               comparison.float_equal(self.y, other.y)

    def __hash__(self):
        """ Calculates hash of vector.

        Test:
        >>> v1 = Vector2(1.0001, 21.0001)
        >>> v2 = Vector2(1.0001, 21.0001)
        >>> v3 = Vector2(1.0001, 21.000100001)
        >>> hash(v1) == hash(v2)
        True
        >>> hash(v1) == hash(v3)
        False
        """
        return hash((self.x, self.y))

    def __mul__(self, scalar):
        """ Scalar multiplication using the * operator. Returns the resulting vector.

        Test:
        >>> v1 = Vector2(1, 2)
        >>> v2 = v1 * 5
        >>> v2.x
        5
        >>> v2.y
        10
        """
        return Vector2(self.x * scalar, self.y * scalar)

    def __str__(self):
        return 'Vector2({:.2f}, {:.2f})'.format(self.x, self.y)

    def __sub__(self, other):
        """ Subtract two vectors using - operator. Returns resulting vector.

        Test:
        >>> v1 = Vector2(1, 4)
        >>> v2 = Vector2(3, 2)
        >>> v3 = v1 - v2
        >>> v3.x
        -2
        >>> v3.y
        2
        """
        return Vector2(self.x - other.x, self.y - other.y)

def reflect_at_line(x1, y1, x2, y2, x3, y3):
    """ Reflects vector 1 at the line between vectors 2 and 3. Returns the x-component 
    and y-component of the reflected vector in this order: reflectAtLine() => x, y

    Parameter:
    x1 -- The x-coordinate of the vector to reflect.
    y1 -- The y-coordinate of the vector to reflect.
    x2 -- The x-coordinate of the first point of the line.
    y2 -- The y-coordinate of the first point of the line.
    x3 -- The x-coordinate of the second point of the line.
    y3 -- The y-coordinate of the second point of the line.
    
    Test:
    >>> x, y = reflect_at_line(-2, -7, -2, 3, 4, -2)
    >>> print('{0:.2f}, {1:.2f}'.format(x, y))
    6.52, 3.23
    >>> x, y = reflect_at_line(-4, 2, 0, -2, 0, 2)
    >>> print('{0:.2f}, {1:.2f}'.format(x, y))
    4.00, 2.00
    """
    # Vector between both points aka the line.
    dx = x3 - x2
    dy = y3 - y2
    
    # Calculate normal with unit length.
    length = pythagorean.solve_c(dy, dx)
    nx = -dy
    ny = dx

    if not comparison.float_equal(length, 0):
        nx /= length
        ny /= length
    
    # Dot product of vector 1 and normal.
    dot_product = x1 * nx + y1 * ny
    
    # The reflected vector.
    x = x1 - 2 * nx * dot_product
    y = y1 - 2 * ny * dot_product
    
    return x, y
        
if __name__ == '__main__':
    print('Executing doctest.')
    import doctest
    doctest.testmod()