value = int(input("Enter a value: "))

hours = value // 3600
minutes = (value % 3600) // 60
seconds = value % 60

print(str(value) + " seconds is equal to " +str(hours) + " : " + str(minutes) + " : " + str(seconds))