
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


x_obs = 4208830.726#float(input("Please enter X-value of the observation point in unit of meters:"))
y_obs = 2334850.0235#float(input("Please enter Y-value of the observation point in unit of meters:"))
z_obs = 4171267.089#float(input("Please enter Z-value of the observation point in unit of meters:"))
print("Given values for observation point are", x_obs, "m for x-axis,", y_obs, "m for y-axis and", z_obs, "m for z-axis.")
phi_obs, lambda_obs, height_obs = xyz2blh(x_obs, y_obs, z_obs)
print("Obtained Longitude value for observation point is: ", lambda_obs, "degree")
print("Obtained Latitude value for observation point is: ", phi_obs, "degree")
print("Obtained height value for observation point is", height_obs, "meters.")

x_tar = 21007733.6107#float(input("Please enter X-value of the target point in unit of meters:"))
y_tar = 15033152.8348#float(input("Please enter Y-value of the target point in unit of meters:"))
z_tar = -7112458.1231#float(input("Please enter Z-value of the target point in unit of meters:"))
print("Given values for target point are", x_tar, "m for x-axis,", y_tar, "m for y-axis and", z_tar, "m for z-axis.")
phi_tar, lambda_tar, height_tar = xyz2blh(x_tar, y_tar, z_tar)
print("Obtained Longitude value for target point is: ", lambda_tar, "degree")
print("Obtained Latitude value for target point is: ", phi_tar, "degree")
print("Obtained height value for target point is", height_tar, "meters.")

obs_values = [phi_obs, lambda_obs, height_obs]
tar_values = [phi_tar, lambda_tar, height_tar]

def global2local(p,r):
    """:arg
    p =  a [3x1] vector that includes the 3D coordinates (𝑥𝑃, 𝑦𝑃, 𝑧𝑃) of the target point whose
    coordinates are intended to be transformed
    r = a [3x1] vector that includes the 3D coordinates (𝑥𝑅, 𝑦𝑅, 𝑧𝑅) of the observation point
    (topocenter).
    :returns
    azimuth_angle_deg = calculated azimuth angle in unit of degrees
    zenith_angle_deg = calculated zenith angle in unit of degrees
    slant = calculated slant range in unit of meters
    """
    [phi_tar, lambda_tar, height_tar] = p
    [phi_obs, lambda_obs, height_obs] = r
    delta_phi = phi_tar - phi_obs
    delta_lambda = lambda_tar - lambda_obs
    a = np.sin(np.deg2rad(delta_phi/2))**2 + np.cos(np.deg2rad(phi_obs))\
        * np.cos(np.deg2rad(phi_tar)) * np.sin(np.deg2rad(delta_lambda/2))**2
    r = 6371000
    d = 2 * r * np.arctan2(a**(1/2), (1-a)**(1/2))
    azimuth_angle_rad = np.arctan2(np.sin(np.deg2rad(delta_lambda)) * np.cos(np.deg2rad(phi_tar)),
                                   np.cos(np.deg2rad(phi_obs))*np.sin(np.deg2rad(phi_tar)) - np.sin(np.deg2rad(phi_obs))
                                   * np.cos(np.deg2rad(phi_tar))* np.cos(np.deg2rad(delta_lambda)))
    azimuth_angle_deg = np.rad2deg(azimuth_angle_rad)
    while True:
        if azimuth_angle_deg < 0:
            azimuth_angle_deg += 360
        else:
            break
    zenith_angle_rad = np.arctan2(height_tar - height_obs, d)
    zenith_angle_deg = np.rad2deg(zenith_angle_rad)
    slant = (((lambda_tar-lambda_obs)**2) + (phi_tar - phi_obs)**2 + (height_tar - height_obs)**2)**0.5
    return [azimuth_angle_deg, zenith_angle_deg, slant]

[azim, zen, r] = global2local(tar_values, obs_values)
print ("Azimuth angle calculated as", azim, "degree.")
print("Zenith angle calculated as", zen, "degree.")
print("Slant range calculated as", r, "meters.")
