total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    # Skip negative numbers
    if number < 0:
        continue

    # End the loop if the user enters 0
    if number == 0:
        break

    total += number

print(f"Sum of positive numbers: {total}")