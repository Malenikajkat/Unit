def binary_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# Пример использования
arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print(f"Элемент {x} находится на позиции {result}")
else:
    print(f"Элемент {x} отсутствует в массиве")
