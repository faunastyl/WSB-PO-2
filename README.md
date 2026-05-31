8. Sklep internetowy z odzieżą – klasy Product, ShoppingCart, Order, Inventory; zarządzanie stanem magazynowym i realizacja koszyka.

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

Aktualnie zaimplementowano:
- Product
- ShoppingCart
- Inventory
- Payment

W kolejnych etapach zostaną dodane:
- Order
- integracja wszystkich klas w głównym programie
