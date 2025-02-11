def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
x = 30
index = linear_search(arr, x)
if index != -1:
    print(f'Элемент {x} найден в массиве на позиции {index}')
else:
    print(f'Элемент {x} отсутствует в массиве')
