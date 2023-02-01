def add_integer(a, b=98):
    try:
        result = a + b
        return int(result)
    except TypeError:
        if type(a) is not int:
            return "a must be an integer"
        else:
            return "b must be an integer"
