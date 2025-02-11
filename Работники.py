import random

# Список работников
workers = ['Иван', 'Петр', 'Анна','Сергей']

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
