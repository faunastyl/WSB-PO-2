from product import Product


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Usunięto {product.name} z magazynu.")
        else:
            print(f"Produkt {product.name} nie znajduje się w magazynie.")

    def check_stock(self, product):
        if product in self.products:
            print(f"{product.name}: {product.stock} szt.")
        else:
            print(f"Produkt {product.name} nie znajduje się w magazynie.")


# ---------- TEST KLASY ----------
if __name__ == "__main__":

    tshirt = Product("T-Shirt", "Black", "M", 79.99, 10)
    bluza = Product("Bluza", "Blue", "L", 149.99, 5)
    spodnie = Product("Spodnie", "Gray", "S", 199.99, 8)

    inventory = Inventory()

    inventory.add_product(tshirt)
    inventory.add_product(bluza)
    inventory.add_product(spodnie)

    inventory.check_stock(tshirt)
    inventory.check_stock(bluza)
    inventory.check_stock(spodnie)

    inventory.remove_product(bluza)

    inventory.check_stock(bluza)
