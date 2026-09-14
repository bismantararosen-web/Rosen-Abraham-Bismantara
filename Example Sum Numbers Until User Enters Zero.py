total = 0
n = float(input("Enter a number (0 to stop): "))

while n != 0.0:
    total += n
    n = float(input("Enter a number (0 to stop): "))

print(f"Sum: {total}")