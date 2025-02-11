def gcd(a, b):
    # Алгоритм Евклида для нахождения НОД
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# Пример использования
num1 = 4
num2 = 6

# Вычисляем НОК
result = lcm(num1, num2)

print(f"Наименьшее общее кратное чисел {num1} и {num2} равно {result}.")
