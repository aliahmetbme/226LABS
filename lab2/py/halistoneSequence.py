while True:
    number = int(input("Please enter a positive integer greater than 1: "))
    if number > 1:
        break

current = number
steps = 0

while current != 1:
    if (steps == 0):
        print(current, end="")
    
    if current % 2 == 0:
        current //= 2
    else:
        current = current * 3 + 1
    
    print(f" → {current}", end="")

    steps += 1

print(f"\nTotal steps: {steps}")
