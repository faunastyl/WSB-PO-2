class Payment:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        print(f"Kwota do zapłaty: {amount:.2f} zł")
        print(f"Wybrana metoda płatności: {self.payment_method}")
        print("Płatność została zrealizowana pomyślnie.")


# TEST KLASY 
if __name__ == "__main__":

    # Przykładowe ceny produktów
    tshirt_price = 80.00
    bluza_price = 190.00
    spodnie_price = 150.00

    # Symulacja zakupu:
    # 2 T-Shirty + 1 Bluza
    total_amount = (2 * tshirt_price) + bluza_price

    payment = Payment("BLIK")
    payment.process_payment(total_amount)
