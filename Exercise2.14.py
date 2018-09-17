
print("Welcome to the distance calculator.  Follow the prompts to calculate the distance between two coordinates!")

x1 , y1 = eval(input("Please enter an x and y coordinate seperated by a comma: "))
x2 , y2 = eval(input("Please enter another x and y coordinate seperated by a comma: "))

xTravel = max(x1, x2) - min(x1, x2)
yTravel = max(y1, y2) - min(y1, y2)
totalDistance = ((xTravel ** 2) + (yTravel) ** 2) ** 0.5

print("The total distance between the two points is:", totalDistance)