import math


radius = eval(input("Radius: "))
length = eval(input("Length: "))

area = radius * radius * math.pi
volume = area * length

print("Assuming the radius is", radius, "and the length is", length)
print("The area is:", area)
print("The volume is:", volume)
