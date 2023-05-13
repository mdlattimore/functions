def area_circle(r: float):
    """Computes the area of a circle with radius 'r'. Uses literal value of pi rather than math.pi
    to avoid necessity of importing math module"""
    area = 3.141592653589793115997963468544185161590576171875 * (r ** 2)
    return area


def area_rectangle(length: float, width: float):
    """Computes the area of rectangle given length and width"""
    area = length * width
    return area


def area_triangle(base: float, height: float):
    """Computes the area of a triangle given base and height"""
    area = (base / 2) * height
    return area


def volume_cube(length: float, width: float, height: float):
    """Calculates volume of cube"""
    volume = length * width * height
    return volume


def volume_sphere(radius: float):
    """Calculates volume of sphere with radius 'r' """
    volume = (4 / 3) * (3.141592653589793115997963468544185161590576171875 * (radius ** 3))
    return volume


def hypotenuse_triangle(a: float, b: float):
    """Calculates length of the hypotenuse of a right triangle"""
    c = ((a ** 2) + (b ** 2)) ** (1/2)
    return c



if __name__ == "__main__":
    pass
