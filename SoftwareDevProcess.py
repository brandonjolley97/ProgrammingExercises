


# This program must let the user input two x and y coordinates.
# After doing so, it must print the distance in the x - direction, y - direction, and total distance between the points.
#
# The input required are two x and y coordinates.
#
# Step 1: Prompt user to input a coordinate in x, y format.  Do this twice.
# Step 2: Calculate distance traveled, in the x and y direction, and the total distance.  This can be done by subtracting the smaller x/y value from the larger x/y value.  The total distance is calculated using pythagoriams theorem.
# Step 3: Print the results by converting the calculated distances to strings.
#
#
#
x1, y1 = eval(input("Please enter a coordinate in x,y format, using only integers: "))
x2, y2 = eval(input("Please enter another coordinate in x,y format: "))

distanceX = max(x1, x2) - min(x1, x2)
distanceY = max(y1, y2) - min(y1, y2)
totalDistance = (distanceX ** 2 + distanceY ** 2) ** 0.5

print("The x - distance traveled is " + str(distanceX) + "," + " the y - distance traveled is " + str(distanceY) + "," + " and the total distance traveled is " + str(totalDistance))