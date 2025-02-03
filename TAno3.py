# Part a: Using nested for loop
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Part b: Using nested while loop
n = 1
while n <= 7:
    if n % 2 != 0:
        print(" " * (5 - n), end="")
        print(str(n) * (2 * n - 1))
    n += 1
