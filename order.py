from shopping_cart import ShoppingCart
from payment import Payment


class Order:
    def __init__(self, cart, payment):
        self.cart = cart
        self.payment = payment

    def place_order(self):
        total = self.cart.calculate_total()

        print("ZAMÓWIENIE")
        print(f"Wartość zamówienia: {total:.2f} zł")

        self.payment.process_payment(total)

        print("Zamówienie zostało złożone.")

  # TEST KLASY

if __name__ == "__main__":

    from product import Product

    tshirt = Product("T-Shirt", "Black", "M", 80.0, 10)
    bluza = Product("Bluza", "Blue", "L", 190.0, 5)

    cart = ShoppingCart()

    cart.add_product(tshirt, 2)
    cart.add_product(bluza, 1)

    payment = Payment("BLIK")

    order = Order(cart, payment)

    order.place_order()
