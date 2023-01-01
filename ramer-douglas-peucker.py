# Ramer - Douglas - Peucker Algorithm

# Specify the file name below between quote symbols ( as a string)
input_file_name = "your file input name in your desktop for example \"line.txt\""

# Specify threshold limit below
epsilon = 6




# Os is required for defining the path of file
import os



# File will be on desktop, so we will start with specifying desktop path
desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
# We will join desktop path and file path to reach file
file_path = os.path.join(desktop_path, input_file_name)


def calculate_distance(point_line_start, point_line_end, point_to_calculate_distance):
    """
    :param point_line_start: starting point of the line in the form of (x,y)
    :param point_line_end: ending point of the line in the form of (x,y)
    :param point_to_calculate_distance: point whose distance to the line calculated, form (x,y)
    :return:
    distance = distance of the given point to the given line
    """
    # Simple linear algebra methods will be used
    # We know that multiplication of slopes of two perpendicular lines is equal to -1
    # Since we know the coordinates of the line we can calculate the slope of the second line
    # print(line_coordinates)
    # print(coordinate)

    x1 = point_line_start[0]
    y1 = point_line_start[1]
    x2 = point_line_end[0]
    y2 = point_line_end[1]
    x3 = point_to_calculate_distance[0]
    y3 = point_to_calculate_distance[1]

    m1 = (y2 - y1) / (x2 - x1)
    m3 = (-1) / m1

    # print("m1=", m1)
    # print("m3 =",m3)

    # Since we know the aim we can find the point of intersection by solving these two lines together
    # Calculate constants for line equations (remember for any (x,y) point on the line y = m*x + n is valid)
    # Chosen point is point_line_start, we will use its values to calculate n

    n1 = y1 - m1 * x1
    # print("n1=", n1)
    # We obtained n1 value, now obtain the n3 value

    n3 = y3 - m3 * x3
    # print("n3=", n3)

    # Solving two lines together for obtaining lines (m1*x + n1 = y = m3*x3 +n3 ==> x = (n1 - n3) / (m3 - m1)

    intersection_x = (n1 - n3) / (m3 - m1)
    intersection_y = m1 * intersection_x + n1
    # print("Intersection x,y =", intersection_x,",", intersection_y)

    # Since we know intersection point and point_to_calculate_distance
    # are on the same line we can directly calculate distance

    distance = ((intersection_x - x3)**2+(intersection_y - y3)**2)**0.5

    return distance

def result_list(coordinates, threshold):
    """
    :param coordinates: coordinates of the lines
    :param threshold: epsilon value (threshold)
    :return:
    output_coordinates = simplified line coordinates
    """

    # We will start with distance 0 and assign calculated maximum distance value
    # Also we need to keep index value, so we will know which point to use if more points needed
    max_distance = 0
    index = 0

    # First and lost points used default, we need to make process among other points
    for i in range(1, len(coordinates)-1):
        # We will calculate distance by using previously defined function
        d = calculate_distance(coordinates[0], coordinates[-1], coordinates[i])
        # Since we are iterating on all points we will find the maximum distance and corresponding index value
        if d > max_distance:
            index = i
            max_distance = d

    # If the specified maximum distance value is bigger than threshold, we will add one more line
    if max_distance > threshold:
        # At the top of if statement we added one more line, now we will recursively calculate between newly added
        #line and before, if needed more lines can be added
        recursion1 = result_list(coordinates[:index+1], epsilon)
        # At the top of if statement we added one more line, now we will recursively calculate between newly added
        # line and after, if needed more lines can be added
        recursion2 = result_list(coordinates[index:], epsilon)
        # Found lines will be concatenated
        concat_values = recursion1[:-1] + recursion2
        return concat_values
    else:
        return [coordinates[0], coordinates[-1]]



# Reading values and turning them into usable x-y coordinates
content = open(file_path, "r")

# Since our input is given as text we read the text first and stripped it to remove "\n" (new line) part
value_list_str = []
for points_str in content:
    value_list_str.append(points_str.strip())
#print(value_list_str)

# Now we have rows, we need to split them
value_list = []
for element in value_list_str:
    value_list.append(element.split(" "))
# print(value_list)

# Type casting from string to integer
value_list_int = []
for values in value_list:
    value_list_int.append([int(values[0]), int(values[1])])
# print(value_list_int)

result_coordinates = result_list(value_list_int, epsilon)
print("Taking input points as:\n\n", value_list_int, "\n\nUsing epsilon value as:\n\n", epsilon,
      "\n\nObtained results are:\n\n", result_coordinates)

