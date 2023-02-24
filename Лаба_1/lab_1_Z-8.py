import random
import math

# Генерируем случайное число в диапазоне от 1 до 10000
n = random.randint(1, 10000)

# Определяем ближайшую степень двойки к числу n
power_of_two = 2**math.ceil(math.log2(n))

# Создаем массив случайных чисел и дополняем его нулями
numbers = [random.randint(1, 100) for _ in range(n)] + [0] * (power_of_two - n)

print(numbers)