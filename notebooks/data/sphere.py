import math
def volume(radius):
    """compute volume of a sphere

    Args:
    radius: float giving the radius of the sphere

    Returns:
    volume of the sphere as a float
    """
    return 4.0/3.0*math.pi*radius**3

def surface_area(radius):
    """compute surface area of a sphere

    Args:
    radius: float giving the radius of the sphere

    Returns:
    surface area of the sphere as a float
    """
    return 4.0*math.pi*radius**2