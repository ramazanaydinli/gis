import math
import numpy as np


def xyz2blh(x, y, z):
    """:arg
    x: x value of cartesian coordinate system in meter unit
    y: y value of cartesian coordinate system in meter unit
    z: z value of cartesian coordinate system in meter unit
        :returns
    lambda_ = Obtained longitude value after iteration
    phi_new = Obtained latitude value after iteration
    height = Obtained height value after iteration
    """
    lambda_ = math.atan(y/x)
    p = (x**2 + y**2)**(1/2)
    a = 6378137
    b = 6356752.3141
    f = 1 - b/a
    e = ((2*f - f**2)**(1/2))
    phi_init = math.atan(z / (p * (1 - e ** 2)))
    phi_old = None
    while True:
        if phi_old is None:
            phi_old = phi_init
        radius_of_curvature = a / ((1 - e**2 * (math.sin(phi_old))**2)**(1/2))
        height = ((p/(math.cos(phi_old))) - radius_of_curvature)
        phi_new = math.atan(z/((1 - e**2 * (radius_of_curvature/(radius_of_curvature+height)))*p))
        diff = np.absolute(np.rad2deg(phi_new-phi_old))
        print("Difference between old and new value is: ", diff)
        if diff < 10**-12:
            print("Difference is: ", diff, "which is smallar than 10^-12, so iteration will stop.")
            break
        else:
            phi_old = phi_new
    return np.rad2deg(phi_new), np.rad2deg(lambda_), height


x = 21007733.6107#float(input("Please enter X-value of the cartesian coordinates in unit of meters:"))
y = 15033152.8348#float(input("Please enter Y-value of the cartesian coordinates in unit of meters:"))
z = -7112458.1231#float(input("Please enter Z-value of the cartesian coordinates in unit of meters:"))
print("Given values are", x , "m for x-axis", y, "m for y-axis and", z, "m for z-axis")
phi_final, lambda_final, height_final = xyz2blh(x, y, z)
print("Obtained Longitude value is: ", lambda_final, "degree")
print("Obtained Latitude value is: ", phi_final, "degree")
print("Obtained height value is", height_final, "meters.")
