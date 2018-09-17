import time

currentTime = time.time()

totalSeconds = int(currentTime)

currentSecond = totalSeconds % 60

totalMinutes = totalSeconds // 60

currentMinute = totalMinutes % 60

totalHours = totalMinutes // 60

currentHour = totalHours % 24

print("Current time is", currentHour, ":", currentMinute, ":", currentSecond, "GMT")
actualTime = eval(input("Please enter the timezone offset from GMT.  Include positive or negative as necessary: "))
print("The current time where you are is", currentHour + actualTime, ":", currentMinute, ":", currentSecond)
