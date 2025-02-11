import random

# Список работников
workers = ['Иван', 'Петр', 'Анна']  # Задание 1: Добавьте нового работника
workers.append('Сергей')

# Спросить у пользователя количество задач
tasks_count = int(input("Сколько задач нужно распределить? "))

# Распределить задачи среди работников
tasks_distribution = {}
for task in range(tasks_count):
    worker = random.choice(workers)
    if worker not in tasks_distribution:
        tasks_distribution[worker] = 1
    else:
        tasks_distribution[worker] += 1

# Вывести результаты распределения задач
print("\nРаспределение задач:")
for worker, tasks in tasks_distribution.items():
    print(f"{worker}: {tasks}")

# Сохранить результаты в файл
with open('task_results.txt', 'w') as file:
    for worker, tasks in tasks_distribution.items():
        file.write(f"{worker}: {tasks}\n")

print("\nРезультаты сохранены в файл 'task_results.txt'.")

# Задание 2: Измените количество задач
additional_runs = int(input("Сколько раз вы хотите повторить запуск программы? "))
for _ in range(additional_runs):
    tasks_count = int(input("Сколько задач нужно распределить? "))
    
    tasks_distribution = {}
    for task in range(tasks_count):
        worker = random.choice(workers)
        if worker not in tasks_distribution:
            tasks_distribution[worker] = 1
        else:
            tasks_distribution[worker] += 1
            
    print("\nРаспределение задач:")
    for worker, tasks in tasks_distribution.items():
        print(f"{worker}: {tasks}")
        
    with open('task_results.txt', 'a') as file:
        file.write(f"\nРезультат распределения задач:\n")
        for worker, tasks in tasks_distribution.items():
            file.write(f"{worker}: {tasks}\n")

# Задание 3: Создайте отчет о проделанной работе
report = input("Напишите краткий отчет о вашей работе над программой: ")
with open('report.txt', 'w') as report_file:
    report_file.write(report)

# Задание 4: Попробуйте изменить способ вывода информации
table_header = "| Работник   | Задачи |\n|-----------|--------|\n"
table_rows = ""
for worker, tasks in tasks_distribution.items():
    table_rows += f"| {worker:<11}| {tasks:^7}|\n"

print(table_header + table_rows)

# Задание 5: Создайте новый файл для хранения данных
with open('tasks_history.txt', 'a') as history_file:
    history_file.write(f"\nРезультат распределения задач:\n")
    for worker, tasks in tasks_distribution.items():
        history_file.write(f"{worker}: {tasks}\n")

# Задание 6: Сделайте программу интерактивной
while True:
    answer = input("Хотите добавить ещё задачи? (да/нет): ")
    if answer.lower() == 'да':
        additional_tasks = int(input("Сколько задач нужно добавить? "))
        for task in range(additional_tasks):
            worker = random.choice(workers)
            if worker not in tasks_distribution:
                tasks_distribution[worker] = 1
            else:
                tasks_distribution[worker] += 1
                
        print("\nРаспределение задач:")
        for worker, tasks in tasks_distribution.items():
            print(f"{worker}: {tasks}")
            
        with open('task_results.txt', 'a') as file:
            file.write(f"\nРезультат распределения задач:\n")
            for worker, tasks in tasks_distribution.items():
                file.write(f"{worker}: {tasks}\n")
    elif answer.lower() == 'нет':
        break
    else:
        print("Не понял ответ. Пожалуйста, введите 'да' или 'нет'")
