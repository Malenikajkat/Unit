def main():
    workers = ["Иван", "Петр", "Анна"]  # Список работников
    earnings = {"Иван": 100, "Петр": 150, "Анна": 200}  # Сколько зарабатывают работники

    total_money = 0  # Общая сумма заработанных денег
    days = 7  # Количество игровых дней

    for day in range(days):
        print(f"День {day + 1}:")
        
        # Выбор работников
        selected_workers = []  # Список выбранных работников
        while True:
            worker = input("Выберите работника (или 'все' для всех): ")  # Попросить выбрать работника
            if worker == "все":  # Если выбрали всех
                selected_workers = workers[:]  # Копируем весь список работников
                break  # Завершаем выбор
            elif worker in workers:  # Если выбрали конкретного работника
                selected_workers.append(worker)  # Добавляем выбранного работника в список
            else:  # Если ввели что-то неправильное
                print("Неизвестный работник. Попробуйте ещё раз.")  # Сообщаем об ошибке

        # Подсчёт заработанных денег
        daily_earnings = sum([earnings[w] for w in selected_workers])  # Суммируем заработок выбранных работников
        total_money += daily_earnings  # Прибавляем к общему заработку
        print(f"Сегодня заработано: {daily_earnings}")  # Показываем, сколько заработали сегодня

        # Сохраняем результаты в файл
        with open("results.txt", "a") as file:  # Открываем файл для добавления данных
            file.write(f"{day + 1},{','.join(selected_workers)},{daily_earnings}\n")  # Записываем данные в файл

    print(f"За {days} дней заработано всего: {total_money}")  # Показываем общий заработок

if __name__ == "__main__":
    main()
