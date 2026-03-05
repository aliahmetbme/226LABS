n = int(input("Please enter a number between 3 and 9: "))

while n < 3 or n > 9:
    n = int(input("Invalid Value.Please enter a number between 3 and 9: "))

for i in range(1, 2 * n):
    k = n - abs(n - i)
    print('*' * k)
