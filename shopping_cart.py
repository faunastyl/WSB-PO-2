from product import Product


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def remove_product(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                print(f"Usunięto {product.name} z koszyka.")
                return

        print(f"Produkt {product.name} nie znajduje się w koszyku.")

    def calculate_total(self):
        total = 0

        for product, quantity in self.items:
            total += product.price * quantity

        return total


# TEST KLASY
if __name__ == "__main__":

    tshirt = Product("T-Shirt", "Black", "M", 79.99, 10)
    hoodie = Product("Hoodie", "Blue", "L", 149.99, 5)

    cart = ShoppingCart()

    cart.add_product(tshirt, 2)
    cart.add_product(hoodie, 1)

    print(f"Wartość koszyka: {cart.calculate_total():.2f} zł")

    cart.remove_product(hoodie)

    print(f"Wartość koszyka po usunięciu produktu: {cart.calculate_total():.2f} zł")
