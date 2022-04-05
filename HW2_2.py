# Задание 2. Задачи на многомерные списки
# В матрице найти номер строки, сумма чисел в которой максимальна.

import random
A = [[random.randint(-10, 10) for i in range(5)] for j in range(5)]
print("Исходная матрица: ", A)
s = []
for i in range(len(A)):
    s.append(sum(A[i]))
print("Строка с наибольшей суммой: ", A[s.index(max(s))], "Сумма элементов: ", max(s))

for index, value in enumerate(s):
    if value == max(s):
        print("Строка с наибольшей суммой: ", f'{index}: {value} ')
