cart = ["T-shirt", "Lamp", "Pen", "Book"]

# Remove "Pen" from the list
cart.remove("Pen")    # ['T-shirt', 'Lamp', 'Book']

# Remove the last item
last_item = cart.pop()
print(cart)   # ['T-shirt', 'Lamp']
print(last_item)    # Book

# Clear the list
cart.clear()
print(cart)    # []
cart = ['T-shirt', 'Lamp', 'Pen', 'Book']

# Delete the third item (index 2)
del cart[2]
print(cart)    # ['T-shirt', 'Lamp', 'Book']