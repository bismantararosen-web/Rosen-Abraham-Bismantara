age = int(input("Enter your age: "))

# Condition to check if age is less than 18
if age < 18:

    # If age is less than 18, condition to check if it's negative
    if age < 0:
        print("Invalid age.")
    else:
        print("Deny access.")
else:
    print("Grant access.")