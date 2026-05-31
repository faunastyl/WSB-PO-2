ZADANIE 2 Bożena Czempas-Chowaniec
Nr 8. Sklep internetowy z odzieżą – klasy Product, ShoppingCart, Order, Inventory; zarządzanie stanem magazynowym i realizacja koszyka.

## Opis projektu

Aplikacja symuluje działanie sklepu internetowego z odzieżą.

Użytkownik może przeglądać produkty, dodawać je do koszyka, wybierać ilość produktów, a następnie złożyć zamówienie i wybrać metodę płatności.

## Funkcjonalności

- zarządzanie produktami odzieżowymi,
- dodawanie i usuwanie produktów z koszyka,
- wybór ilości produktów,
- obliczanie wartości koszyka,
- kontrola stanów magazynowych,
- składanie zamówień,
- obsługa płatności.

## Diagram UML

Diagram klas znajduje się w folderze `UML`.

## Klasy projektu
- product.py – klasa Product
- shopping_cart.py – klasa ShoppingCart
- inventory.py – klasa Inventory
- payment.py – klasa Payment
- order.py – klasa Order
- sklep.py – program główny
  
### Product
Reprezentuje produkt dostępny w sklepie.

Atrybuty:
- nazwa,
- kolor,
- rozmiar,
- cena,
- stan magazynowy.

### ShoppingCart
Odpowiada za zarządzanie koszykiem zakupowym.

Funkcje:
- dodawanie produktów,
- usuwanie produktów,
- obliczanie wartości koszyka.

### Inventory
Przechowuje informacje o produktach dostępnych w magazynie.

### Payment
Obsługuje metody płatności:
- karta,
- BLIK,
- przelew.

### Order
Reprezentuje zamówienie klienta.

## Logika działania systemu

1. Produkty są przechowywane w magazynie.
2. Klient dodaje produkty do koszyka.
3. System sprawdza dostępność produktów.
4. Obliczana jest wartość koszyka.
5. Klient wybiera metodę płatności.
6. Tworzone jest zamówienie.
7. Stan magazynowy zostaje zaktualizowany.

## Testowanie

Każda klasa będzie testowana oddzielnie podczas implementacji.

## Status projektu

Zaimplementowane klasy:

- Product
- ShoppingCart
- Inventory
- Payment
- Order

Program główny:

- sklep.py

#Przykładowy scenariusz działania

1. Produkty są dodawane do magazynu.
2. Klient dodaje produkty do koszyka.
3. Obliczana jest wartość koszyka.
4. Klient wybiera metodę płatności.
5. Tworzone jest zamówienie.
6. Zamówienie zostaje zrealizowane.

#### Autor: Bożena Czempas-Chowaniec
