import tkinter as tk
from tkinter import messagebox

# Данные о работниках
workers = ["Иван", "Петр", "Анна"]
earnings = {"Иван": 100, "Петр": 150, "Анна": 200}

class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Игра 'Работники'")
        self.geometry("300x250")

        self.total_money = 0
        self.days = 7
        self.day = 1

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        self.title_label = tk.Label(self, text=f"День {self.day}:", font=("Arial", 14))
        self.title_label.pack(pady=10)

        # Кнопки для выбора работников
        self.worker_buttons = {}
        for worker in workers:
            button = tk.Button(self, text=f"{worker}", command=lambda w=worker: self.select_worker(w))
            button.pack(pady=5)
            self.worker_buttons[worker] = button

        # Кнопка "Все"
        all_button = tk.Button(self, text="Все", command=self.select_all_workers)
        all_button.pack(pady=5)

        # Кнопка "Следующий день"
        next_day_button = tk.Button(self, text="Следующий день", command=self.next_day)
        next_day_button.pack(pady=20)

    def select_worker(self, worker):
        if worker not in self.selected_workers:
            self.selected_workers.add(worker)
            self.worker_buttons[worker].config(bg="green")

    def select_all_workers(self):
        for worker in workers:
            if worker not in self.selected_workers:
                self.select_worker(worker)

    def calculate_daily_earnings(self):
        daily_earnings = sum([earnings[w] for w in self.selected_workers])
        return daily_earnings

    def save_results_to_file(self, daily_earnings):
        with open("results.txt", "a") as file:
            file.write(f"{self.day},{','.join(sorted(self.selected_workers))},{daily_earnings}\n")

    def next_day(self):
        if self.day >= self.days:
            messagebox.showinfo("Конец игры", f"За {self.days} дней заработано всего: {self.total_money}")
            self.destroy()
            return

        daily_earnings = self.calculate_daily_earnings()
        self.save_results_to_file(daily_earnings)
        self.total_money += daily_earnings

        self.day += 1
        self.selected_workers.clear()
        for button in self.worker_buttons.values():
            button.config(bg="SystemButtonFace")

        self.title_label.config(text=f"День {self.day}:")

    def start_game(self):
        self.selected_workers = set()
        self.mainloop()

if __name__ == "__main__":
    app = GameApp()
    app.start_game()
