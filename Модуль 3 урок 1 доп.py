import tkinter as tk
import random

# Основные параметры игры
CARD_SIZE = 4  # Размер игрового поля: 4x4
NUM_PAIRS = (CARD_SIZE * CARD_SIZE) // 2

def binary_search(arr, target):
    """Функция бинарного поиска"""
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

class PairGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра «Уничтожить пару»")
        self.buttons = []
        self.first_card = None
        self.second_card = None

        # Создаем список с парами элементов
        self.cards = list(range(NUM_PAIRS)) * 2
        random.shuffle(self.cards)

        # Создаем кнопки игрового поля
        for i in range(CARD_SIZE):
            button_row = []
            for j in range(CARD_SIZE):
                btn = tk.Button(self.root, text="?", width=8, height=4,
                                command=lambda row=i, col=j: self.reveal_card(row, col))
                btn.grid(row=i, column=j)
                button_row.append(btn)
            self.buttons.append(button_row)

    def reveal_card(self, row, col):
        if self.first_card and self.second_card:
            return  # Игнорируем нажатия, если уже выбраны две карточки

        btn = self.buttons[row][col]
        if btn["text"] == "?":
            btn["text"] = str(self.cards[row * CARD_SIZE + col])
            btn["state"] = "disabled"
            if not self.first_card:
                self.first_card = (row, col)
            elif not self.second_card:
                self.second_card = (row, col)
                self.root.after(1000, self.check_match)

    def is_pair_found(self, card_value):
        """Проверяет, найдена ли пара для данной карты."""
        pair_index = self.cards.index(card_value) + 1
        if pair_index < len(self.cards) and self.cards[pair_index] == card_value:
            return True
        return binary_search(self.cards[pair_index:], card_value)

    def check_match(self):
        r1, c1 = self.first_card
        r2, c2 = self.second_card
        first_card_value = self.cards[r1 * CARD_SIZE + c1]
        second_card_value = self.cards[r2 * CARD_SIZE + c2]

        if first_card_value == second_card_value:
            self.buttons[r1][c1]["bg"] = "green"
            self.buttons[r2][c2]["bg"] = "green"
            if self.is_pair_found(first_card_value):
                print(f"Пара {first_card_value} найдена!")
        else:
            self.buttons[r1][c1]["text"] = "?"
            self.buttons[r2][c2]["text"] = "?"
            self.buttons[r1][c1]["state"] = "normal"
            self.buttons[r2][c2]["state"] = "normal"

        self.first_card = None
        self.second_card = None

if __name__ == "__main__":
    root = tk.Tk()
    game = PairGame(root)
    root.mainloop()
