text = input("Enter a string: ")

digit_sum = 0

for char in text:
    if char.isdigit():
        digit_sum += int(char)

print("Sum of digits:", digit_sum)
