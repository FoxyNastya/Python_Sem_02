'''Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
'''
import random
from collections import Counter
n = int(input("Введите количество монеток: "))
pillow = [random.randint(0, 1) for x in range(n)]
counter0 = pillow.count(0)
counter1 = pillow.count(1)

print(*pillow, sep=', ')

if counter0 < counter1:
    print(f'Необходимо перевернуть все монетки со значением 0, т.к. их меньше всего, а именно: {counter0}')
elif counter0 == counter1:
    print(f'Выпало одинаковое количество монеток со значением 0 и 1, а именно: {counter0}')
else:
    print(f'Необходимо перевернуть все монетки со значением 1, т.к. их меньше всего, а именно: {counter1}')
