passcode = "1345"
entered_code = input("Enter passcode: ")

result = (passcode == entered_code)
print(f"Is passcode equal to entered code? {result}")

result = not (passcode == entered_code)
print(f"Is passcode not equal to entered code? {result}")