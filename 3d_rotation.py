import numpy as np


def rotation(vec, ang, ax):
    """:arg
    vec = a [1x3] or [3x1] vector that includes X, Y, Z coordinates of the defined point in the first system
    ang = rotation angle in degree
    ax = rotation axis (1,2 or 3) (x-axis will be labeled by 1, y will be labeled by 2 and z will be labeled by 3)"""
    if ax == 1:
        rotation_matrix = np.matrix([[1, 0, 0], [0, np.cos(np.deg2rad(ang)), np.sin(np.deg2rad(ang))], [0, -np.sin(np.deg2rad(ang)), np.cos(np.deg2rad(ang))]])
    elif ax == 2:
        rotation_matrix = np.matrix([[np.cos(np.deg2rad(ang)), 0, -np.sin(np.deg2rad(ang))], [0, 1, 0], [np.sin(np.deg2rad(ang)), 0, np.cos(np.deg2rad(ang))]])
    elif ax == 3:
        rotation_matrix = np.matrix([[np.cos(np.deg2rad(ang)), np.sin(np.deg2rad(ang)), 0], [-np.sin(np.deg2rad(ang)), np.cos(np.deg2rad(ang)), 0],[0, 0, 1]])
    rotated_matrix = np.matmul(rotation_matrix, vec)
    return rotated_matrix


def get_input_vector():
    "This function will take x,y,z values of input vector and save them for later usage"

    print("Please provide vector you want to rotate by using x,y,z coordinates respectively")
    input_vector = []
    input_x = float(input("Please provide vector's x value:"))
    input_vector.append(input_x)
    input_y = float(input("Please provide vector's y value:"))
    input_vector.append(input_y)
    input_z = float(input("Please provide vector's z value:"))
    input_vector.append(input_z)
    print("Your input vector is ", input_vector)

    return input_vector


def get_input_axis():
    "This function will take the input axis to rotate on and return it later usage"

    while True:
        input_axis = int(input("Please provide the axis you want to rotate on(for x please write 1,"
                                " for y write 2 and for z write 3): "))
        if input_axis == 1:
            rotation_axis_name = "x"
            break
        elif input_axis == 2:
            rotation_axis_name = "y"
            break
        elif input_axis == 3:
            rotation_axis_name = "z"
            break
        else:
            print("You typed wrong axis number, please provide an appropriate axis "
                  "(for x choose 1, for y choose 2, for z choose 3)")
    print("You choose", input_axis, ", your rotation will be done on", rotation_axis_name, "axis.")
    return input_axis, rotation_axis_name


def get_input_angle():
    "This function will take input angle and return it for later usage"

    input_angle = int(input("Please enter how many degrees you want to rotate"
                            "(+ for counter-clockwise, - for clockwise): "))
    print("You choose", input_angle, "degree for rotation")
    return input_angle


input_vector = get_input_vector()


while True:
    input_axis, rotation_axis_name = get_input_axis()
    input_angle = get_input_angle()

    print("To bring all together, your input vector", input_vector, "will be rotated on", rotation_axis_name, "axis",
              "by", input_angle, "degrees.")
    nvec = rotation(input_vector, input_angle, input_axis)
    print("After rotation your new vector calculated as: ", nvec)
    input_continue = input("If you want to perform another rotation operation please type 'Y', "
                               "other answers will terminate the program: ")
    if input_continue == "Y":
        input_vector = nvec.reshape((3,1))
        continue
    else:
        break

