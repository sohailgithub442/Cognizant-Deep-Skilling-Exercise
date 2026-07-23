"""
Code Review Demo
Topic: Leave 3+ Structured PR Comments
"""

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total

    def display_items(self):
        print("Shopping Cart")
        for item in self.items:
            print(f"{item['name']} - ₹{item['price']}")
        print(f"Total: ₹{self.calculate_total()}")


cart = ShoppingCart()
cart.add_item("Laptop", 65000)
cart.add_item("Mouse", 1200)
cart.add_item("Keyboard", 2500)
cart.display_items()


"""
Sample Pull Request Review Comments

PR Comment 1:
Suggestion:
Use Python's built-in sum() function in calculate_total()
to improve readability and reduce manual iteration.

PR Comment 2:
Nit:
Consider validating that price is a positive number before
adding an item to the cart.

PR Comment 3:
Suggestion:
Move the print statements into a separate UI layer so the
ShoppingCart class focuses only on business logic.

PR Comment 4:
Style:
Add type hints and docstrings for better maintainability.
"""
