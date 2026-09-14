attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == "1212":
        print("Access granted.")
        break

    attempts -= 1
    print(f"Wrong PIN. {attempts} tries left.")
else:
    print("Account locked. Too many failed attempts.")