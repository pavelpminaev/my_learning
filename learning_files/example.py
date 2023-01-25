"""It's example doctest using"""

def reverse(string):
    """Reverse string.
    >>> reverse('')
    ''
    >>> reverse('Hexlet')
    'telxeH'
    """
    return string[::-1]


# Нужно для запуска тестов
if __name__ == "__main__":
    import doctest
    doctest.testmod()
