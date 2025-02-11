def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Пример использования
number1 = 4
number2 = 6

# Вычисляем НОД
result = gcd(number1, number2)

print(f"Наибольший общий делитель чисел {number1} и {number2} равен {result}.")
