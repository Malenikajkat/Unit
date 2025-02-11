import tkinter as tk
from tkinter import messagebox
import random

# Функция для распределения задач
def distribute_tasks():
    global workers, tasks_count, tasks_distribution
    
    tasks_count = int(entry_tasks.get())
    
    tasks_distribution = {}
    for task in range(tasks_count):
        worker = random.choice(workers)
        if worker not in tasks_distribution:
            tasks_distribution[worker] = 1
        else:
            tasks_distribution[worker] += 1
    
    text_result.delete('1.0', tk.END)
    text_result.insert(tk.END, "\nРаспределение задач:\n")
    for worker, tasks in tasks_distribution.items():
        text_result.insert(tk.END, f"{worker}: {tasks}\n")
    
    save_to_file()

# Функция для сохранения результатов в файл
def save_to_file():
    with open('task_results.txt', 'w') as file:
        for worker, tasks in tasks_distribution.items():
            file.write(f"{worker}: {tasks}\n")
    
    messagebox.showinfo("Успешно!", "Результаты сохранены в файл 'task_results.txt'.")

# Функция для добавления нового работника
def add_worker():
    new_worker = entry_new_worker.get().strip()
    if new_worker:
        workers.append(new_worker)
        listbox_workers.delete(0, tk.END)
        for worker in workers:
            listbox_workers.insert(tk.END, worker)
        entry_new_worker.delete(0, tk.END)

# Функция для повторного запуска программы
def repeat_program():
    additional_runs = int(entry_repeat.get())
    for _ in range(additional_runs):
        tasks_count = int(entry_tasks.get())
        
        tasks_distribution = {}
        for task in range(tasks_count):
            worker = random.choice(workers)
            if worker not in tasks_distribution:
                tasks_distribution[worker] = 1
            else:
                tasks_distribution[worker] += 1
                
        text_result.delete('1.0', tk.END)
        text_result.insert(tk.END, "\nРаспределение задач:\n")
        for worker, tasks in tasks_distribution.items():
            text_result.insert(tk.END, f"{worker}: {tasks}\n")
            
        with open('task_results.txt', 'a') as file:
            file.write(f"\nРезультат распределения задач:\n")
            for worker, tasks in tasks_distribution.items():
                file.write(f"{worker}: {tasks}\n")

# Функция для создания отчета
def create_report():
    report = textarea_report.get('1.0', tk.END).strip()
    if report:
        with open('report.txt', 'w') as report_file:
            report_file.write(report)
        messagebox.showinfo("Успешно!", "Ваш отчет был сохранен.")

# Функция для интерактивного добавления задач
def interactive_addition():
    while True:
        answer = messagebox.askyesno("Добавить задачи?", "Хотите добавить ещё задачи?")
        if answer:
            additional_tasks = int(messagebox.askstring("Количество задач", "Сколько задач нужно добавить?"))
            for task in range(additional_tasks):
                worker = random.choice(workers)
                if worker not in tasks_distribution:
                    tasks_distribution[worker] = 1
                else:
                    tasks_distribution[worker] += 1
                    
            text_result.delete('1.0', tk.END)
            text_result.insert(tk.END, "\nРаспределение задач:\n")
            for worker, tasks in tasks_distribution.items():
                text_result.insert(tk.END, f"{worker}: {tasks}\n")
                
            with open('task_results.txt', 'a') as file:
                file.write(f"\nРезультат распределения задач:\n")
                for worker, tasks in tasks_distribution.items():
                    file.write(f"{worker}: {tasks}\n")
        else:
            break

# Главная функция приложения
def main():
    global root, workers, tasks_count, tasks_distribution
    global entry_tasks, entry_new_worker, entry_repeat, listbox_workers, text_result, textarea_report
    
    workers = ['Иван', 'Петр', 'Анна', 'Сергей']
    tasks_count = 0
    tasks_distribution = {}
    
    root = tk.Tk()
    root.title("Распределение задач")
    
    # Фрейм для ввода количества задач
    frame_tasks = tk.Frame(root)
    label_tasks = tk.Label(frame_tasks, text="Введите количество задач:", font=("Arial", 14))
    entry_tasks = tk.Entry(frame_tasks, width=10, font=("Arial", 14))
    button_distribute = tk.Button(frame_tasks, text="Распределить задачи", command=distribute_tasks, font=("Arial", 14))
    
    label_tasks.pack(side=tk.LEFT, padx=(10, 5), pady=10)
    entry_tasks.pack(side=tk.LEFT, padx=5, pady=10)
    button_distribute.pack(side=tk.LEFT, padx=5, pady=10)
    
    frame_tasks.pack(fill=tk.X, pady=(10, 0))
    
    # Фрейм для списка работников
    frame_workers = tk.Frame(root)
    label_workers = tk.Label(frame_workers, text="Список работников:", font=("Arial", 14))
    listbox_workers = tk.Listbox(frame_workers, height=len(workers), width=15, font=("Arial", 14))
    scrollbar_workers = tk.Scrollbar(frame_workers, orient=tk.VERTICAL)
    
    for worker in workers:
        listbox_workers.insert(tk.END, worker)
    
    listbox_workers.config(yscrollcommand=scrollbar_workers.set)
    scrollbar_workers.config(command=listbox_workers.yview)
    
    label_workers.pack(side=tk.LEFT, padx=10, pady=10)
    listbox_workers.pack(side=tk.LEFT, padx=5, pady=10)
    scrollbar_workers.pack(side=tk.LEFT, fill=tk.Y, pady=10)
    
    frame_workers.pack(fill=tk.X, pady=(10, 0))
    
    # Фрейм для добавления нового работника
    frame_new_worker = tk.Frame(root)
    label_new_worker = tk.Label(frame_new_worker, text="Добавить нового работника:", font=("Arial", 14))
    entry_new_worker = tk.Entry(frame_new_worker, width=15, font=("Arial", 14))
    button_add_worker = tk.Button(frame_new_worker, text="Добавить", command=add_worker, font=("Arial", 14))
    
    label_new_worker.pack(side=tk.LEFT, padx=10, pady=10)
    entry_new_worker.pack(side=tk.LEFT, padx=5, pady=10)
    button_add_worker.pack(side=tk.LEFT, padx=5, pady=10)
    
    frame_new_worker.pack(fill=tk.X, pady=(10, 0))
    
    # Фрейм для повтора программы
    frame_repeat = tk.Frame(root)
    label_repeat = tk.Label(frame_repeat, text="Повторить программу:", font=("Arial", 14))
    entry_repeat = tk.Entry(frame_repeat, width=10, font=("Arial", 14))
    button_repeat = tk.Button(frame_repeat, text="Повторить", command=repeat_program, font=("Arial", 14))
    
    label_repeat.pack(side=tk.LEFT, padx=10, pady=10)
    entry_repeat.pack(side=tk.LEFT, padx=5, pady=10)
    button_repeat.pack(side=tk.LEFT, padx=5, pady=10)
    
    frame_repeat.pack(fill=tk.X, pady=(10, 0))
    
    # Фрейм для отчета
    frame_report = tk.Frame(root)
    label_report = tk.Label(frame_report, text="Напишите отчет:", font=("Arial", 14))
    textarea_report = tk.Text(frame_report, width=50, height=5, font=("Arial", 14))
    button_save_report = tk.Button(frame_report, text="Сохранить отчет", command=create_report, font=("Arial", 14))
    
    label_report.pack(side=tk.LEFT, padx=10, pady=10)
    textarea_report.pack(side=tk.LEFT, padx=5, pady=10)
    button_save_report.pack(side=tk.LEFT, padx=5, pady=10)
    
    frame_report.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
    
    # Фрейм для результата
    frame_result = tk.Frame(root)
    label_result = tk.Label(frame_result, text="Результат:", font=("Arial", 14))
    text_result = tk.Text(frame_result, width=50, height=10, font=("Arial", 14))
    scrollbar_result = tk.Scrollbar(frame_result, orient=tk.VERTICAL)
    
    text_result.config(yscrollcommand=scrollbar_result.set)
    scrollbar_result.config(command=text_result.yview)
    
    label_result.pack(side=tk.LEFT, padx=10, pady=10)
    text_result.pack(side=tk.LEFT, padx=5, pady=10)
    scrollbar_result.pack(side=tk.LEFT, fill=tk.Y, pady=10)
    
    frame_result.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
    
    # Кнопка для интерактивного добавления задач
    button_interactive = tk.Button(root, text="Интерактивное добавление задач", command=interactive_addition, font=("Arial", 14))
    button_interactive.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
