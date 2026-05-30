class Product:
    def __init__(self, name, color, size, price, stock):
        self.name = name
        self.color = color
        self.size = size
        self.price = price
        self.stock = stock


# Test klasy Product
tshirt = Product("T-Shirt", "Black", "M", 79.99, 10)

print("Produkt:")
print(f"Nazwa: {tshirt.name}")
print(f"Kolor: {tshirt.color}")
print(f"Rozmiar: {tshirt.size}")
print(f"Cena: {tshirt.price} zł")
print(f"Stan magazynowy: {tshirt.stock}")
