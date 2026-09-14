age = int(input("Enter your age: "))
citizen = input("U.S. citizen (yes/no)?: ")

# True if either (age >= 18)
# or
# (citizen == "yes") is True
result = (age >= 18) or (citizen == "yes")
print(result)