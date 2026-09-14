stock = ['Laptop', 'Keyboard', 'Mouse']

order = input("Enter the product you want to buy: ")

for product in stock:
    if product == order:
        print(f"{order} is available. Adding to cart.")
        break
else:
    print(f"Sorry, {order} is out of stock.")
Run Code
