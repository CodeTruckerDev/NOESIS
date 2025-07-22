#!/usr/bin/python3

import os
import random
from string import ascii_letters, digits

class CovSecure:
    def __init__(self):
        self.chars = ascii_letters + digits # lower row string
        self.specials = "!@#$%^&*(){}[]?"   # token - mid row
        self.word_length = 30
        
        self.word = self._generate_word()        

        self.colors = {
            'red':    "\033[1;31m",
            'blue':   "\033[1;34m",
            'purple': "\033[1;35m",
            #'cyan':   "\033[1;36m",
            'green':  "\033[1;32m",
            'yellow': "\033[1;33m"
        }
        self.end_color = '\033[0m'
        
        self.color_order = self._shuffle_colors()
        self.trigger_color_name = self._get_trigger_color()

        self.specials_line = self._generate_specials_line()
        
        self.colored_line = self._generate_colored_line()
        self.password = self.generate_password()

    def display_color_bar(self):
        #print("Kolorowy pasek (trigger jest w środku):\n")
        for color in self.color_order:
            print(f"{self.colors[color]} █ {self.end_color}", end=" ")
        print("\n")

    def _generate_specials_line(self):
        specials_list = list(self.specials)
        random.shuffle(specials_list)
        return specials_list

    def display_specials_line(self):
        #print("Środkowy rząd (znaki specjalne):\n")
        for ch in self.specials_line:
            print(f"{ch}", end=" ")
        print("\n")

    def generate_password(self):
        filtered_chars = [ch for ch, color in self.colored_line
                          if color == self.trigger_color_name]

        count = len(filtered_chars)          # „miejsce” dla użytkownika
        if count == 0:
            # Decyzja projektowa – brak znaków triggera:
            # Możemy np. natychmiast zakończyć lub użyć pierwszego tokena.
            position_index = 0
        else:
            position_index = count - 1       # konwersja na indeks 0-based

        if position_index >= len(self.specials_line):
            position_index = len(self.specials_line) - 1

        token = self.specials_line[position_index]
        final_password = ''.join(filtered_chars) + token
        return final_password



    def _generate_colored_line(self):
        result = []
        for _ in range(self.word_length):
            char = random.choice(self.chars)
            color = random.choice(self.color_order)
            result.append((char, color))
        return result

    def display_colored_line(self):
        #print("Dolny rząd (kolorowe znaki):\n")
        for ch, color in self.colored_line:
            print(f"{self.colors[color]}{ch}{self.end_color}", end="")
        print("\n")


    def _generate_word(self):
        return ''.join(random.choice(self.chars) for _ in range(self.word_length))

    def _shuffle_colors(self):
        color_list = list(self.colors.keys())
        random.shuffle(color_list)
        return color_list

    def _get_trigger_color(self):
        return self.color_order[len(self.color_order) // 2]

    def clear_screen(self):
        os.system('clear')  # użyj 'cls' jeśli chcesz testować na Windowsie

    def display_prompt(self):
        prompts = [
            "W sercu palindromu, gdzie lustro łamie się na pół, znajdziesz tego, który nie ma odbicia.",
            "Tam gdzie pierwszy oddech spotyka się z ostatnim tchnieniem, w ciszy między nimi mieszka prawda.",
            "W miejscu, gdzie echo wraca do swojego źródła, lecz jeszcze nie dotarło do celu, tam kryje się klucz.",
            "Gdzie równowaga trzyma w dłoniach początek i koniec, jej serce bije w rytmie ukrytej melodii.",
            "W punkcie, gdzie droga naprzód staje się drogą powrotną, tam mieszka ten, który nigdy się nie porusza."
        ]
        print(random.choice(prompts))
        print()


    def debug_info(self):
        print(f"[DEBUG] Kolor wyzwalający: {self.trigger_color_name}\n")

    def show_password_debug(self):
        filtered_chars = [ch for ch, color in self.colored_line
                  if color == self.trigger_color_name]
        count = len(filtered_chars)
        position_index = max(0, min(count - 1, len(self.specials_line) - 1))
        token = self.specials_line[position_index]
        print(f"[DEBUG] Wygenerowane hasło: {self.password}")
        print(f"[DEBUG] Długość hasła bez tokena: {len(self.password)-1} znaków")
        print(f"[DEBUG] Token to znak '{token}' z pozycji {count} w specials_line")


# --- Główne uruchomienie ---

if __name__ == "__main__":
    cov = CovSecure()
    cov.clear_screen()
    cov.display_prompt()            # 🔮 nowy etap
    
    cov.display_color_bar()         # Górny pasek z kolorami
    cov.display_specials_line()     # Środkowy rząd z tokenami
    cov.display_colored_line()      # Dolny rząd z kolorowymi znakami
    
    cov.debug_info()
    cov.show_password_debug()       # [DEBUG] poprawne hasło
