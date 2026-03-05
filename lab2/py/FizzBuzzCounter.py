number = int(input("Please enter a number between 10 and 100: "))
while number < 10 or number > 100:
    number = int(input("Invalid input. Please enter a number between 10 and 100: "))

fizzCount = 0
buzzCount = 0
fizzBuzzCount = 0

for i in range(1, number + 1):
    if i % 7 == 0:
        print(f"({i} is skipped)")
        continue
    elif i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
        fizzBuzzCount += 1
    elif i % 5 == 0:
        print("Buzz")
        buzzCount += 1
    elif i % 3 == 0:
        print("Fizz")
        fizzCount += 1
    else:
        print(i)

print("\n--- Summary ---")
print(f"Fizz count: {fizzCount}")
print(f"Buzz count: {buzzCount}")
print(f"FizzBuzz count: {fizzBuzzCount}")