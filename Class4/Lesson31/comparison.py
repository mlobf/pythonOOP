"""
    Comparison Magic Methods

    __eq__ => ==
    __ne__ => !=
    __gt__ => >
    __lt__ => <
    __ge__ => >=
    __le__ => <=

"""

x = -2
y = -2

# Functional aproach


def comparison(x: int = 0, y: int = 0):
    result = int(x) == int(y)
    # return result
    return print(result)


comparison(x, y)
