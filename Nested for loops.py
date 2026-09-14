attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Porsche', 'Mercedes']

# Outer loop
for attribute in attributes:
    # Inner loop
    for car in cars:
        print(attribute, car)
    
    # This statement is outside the inner loop
    print("-----")
  