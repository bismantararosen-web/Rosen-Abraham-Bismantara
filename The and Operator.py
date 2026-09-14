age = int(input("Enter your age: "))
citizen = input("U.S. citizen (yes/no)?: ")

# True only if (age >= 18) 
# and
# (citizen == "yes") is True
result = (age >= 18) and (citizen == "yes")
print(result)