favorite_items = ["T-shirt", "Lamp", "Pen"]

size = len(favorite_items)
print(size)   # 3
cart = ["T-shirt", "Lamp", "Pen"]

result = "Lamp" in cart
print(result)   # True

result = "Book" in cart
print(result)   # False
cart_items = ["T-shirt", "Lamp", "Pen"]

for item in cart_items:
    print(item)