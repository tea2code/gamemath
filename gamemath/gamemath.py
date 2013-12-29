def int_round(number):
    """ Round to the nearest integer. See
    http://www.daniweb.com/software-development/python/threads/299459/round-to-nearest-integer
    for more information.

    Test:
    >>> int_round(4.9)
    5
    >>> int_round(5.1)
    5
    >>> int_round(-4.9)
    -5
    >>> int_round(-5.1)
    -5
    >>> int_round(0.5)
    1
    >>> int_round(-0.5)
    -1
    >>> int_round(0.4999999)
    0
    >>> int_round(-0.4999999)
    0
    """
    if number > 0:
        return int(number + 0.5)
    else:
        return int(number - 0.5)

if __name__ == '__main__':
    print('Executing doctest.')
    import doctest
    doctest.testmod()