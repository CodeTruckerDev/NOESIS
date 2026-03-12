# NOESIS

Terminalowa aplikacja generująca wizualne, jednorazowe hasło oparte na losowym kolorze wyzwalającym i tokenie specjalnym.  
Kontynuacja pomysłu z [Project-X](https://github.com/CodeTruckerDev/Project-X) – bardziej złożona, rytualna wersja zagadki z kolorami i enigmatycznymi podpowiedziami.
To druga iteracja pomysłu na wizualny, jednorazowy klucz bez zapisywania danych.

W porównaniu do Project-X dodałem losowy trigger (zamiast jednego stałego), trzy rzędy wizualne, token zależny od liczby triggerów i rytualne podpowiedzi.
Został w formie, w jakiej powstał – bez zmian i bez upiększania.

## Co robi

- Losuje 30-znakowy ciąg znaków (litery + cyfry)
- Losowo przypisuje 5 kolorów ANSI (czerwony, niebieski, fiolet, zielony, żółty) do znaków
- Wybiera wyzwalający kolor z środka przetasowanej listy kolorów
- Tworzy środkowy rząd z 7 losowo przetasowanymi znakami specjalnymi (!@#$%^&*() itd.)
- Wyświetla trzy rzędy: pasek kolorów, znaki specjalne, kolorowy ciąg
- Hasło = wszystkie znaki w kolorze wyzwalającym + jeden token specjalny z pozycji zależnej od liczby triggerów
- Pokazuje enigmatyczną, poetycką podpowiedź (losowaną z 5 fraz)

## Wymagania

Python 3 (standardowa biblioteka + os, random, string)

## Uruchomienie

```bash
python main.py
```
