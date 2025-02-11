# Функция сортировки пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Пример использования
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Исходный список:", my_list)

# Вызываем функцию для сортировки
bubble_sort(my_list)

# Выводим отсортированный список
print("Отсортированный список:", my_list)
