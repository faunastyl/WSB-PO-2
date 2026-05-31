from product import Product
from shopping_cart import ShoppingCart
from inventory import Inventory
from payment import Payment
from order import Order


# Produkty
tshirt = Product("T-Shirt", "Black", "M", 80.0, 10)
bluza = Product("Bluza", "Blue", "L", 190.0, 5)
spodnie = Product("Spodnie", "Gray", "S", 150.0, 8)

# Magazyn
inventory = Inventory()

inventory.add_product(tshirt)
inventory.add_product(bluza)
inventory.add_product(spodnie)

print("Dostępne produkty:")

inventory.check_stock(tshirt)
inventory.check_stock(bluza)
inventory.check_stock(spodnie)

# Koszyk
cart = ShoppingCart()

cart.add_product(tshirt, 2)
cart.add_product(bluza, 1)

print()
print(f"Wartość koszyka: {cart.calculate_total():.2f} zł")
print()

# Płatność
payment = Payment("BLIK")

# Zamówienie
order = Order(cart, payment)

order.place_order()
