cart = ["T-shirt", "Lamp", "Pen"]

# Update second item to "Shoes"
cart[1] = "Shoes"

print(cart)    # ['T-shirt', 'Shoes', 'Pen']
cart = ["T-shirt", "Lamp", "Pen"]

# Add "Book" to the list
cart.append("Book")

print(cart)    # ['T-shirt', 'Lamp', 'Pen', 'Book']
cart = ["T-shirt", "Lamp", "Pen"]
fav_items = ["Headphones", "Phone"]

# Add all the items from fav_items to cart
cart.extend(fav_items)

print(cart)    # ['T-shirt', 'Lamp', 'Pen', 'Headphones', 'Phone']
cart = ["T-shirt", "Lamp", "Pen"]

# Add "Book" at index 2 (3rd position)
cart.insert(2, "Book")

print(cart)    # ['T-shirt', 'Lamp', 'Book', 'Pen']