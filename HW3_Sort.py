import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика

# 1. Функция для сортировки пузырьком bubble:
def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a

# 2. Функция сортировки вставками insert:
def InsertSort(A):
    for i in range(1, len(A)):
        t = A[i]
        j = i
        while j > 0 and A[j - 1] > t:  # вместо j >= 0 нужно j > 0
            A[j] = A[j - 1]
            j -= 1
        A[j] = t

# 3. Функция шейкерной (коктейльной) сортировки shaker -
# модификация пузырьковой:
def ShakerSort(A):
    # while True:
    #     for i in (range(len(A) - 1), reversed(range(len(A) - 1))):
    #         swapped = False
    #         for j in i:
    #             if A[j] > A[j + 1]:
    #                 A[j], A[j + 1] = A[j + 1], A[j]
    #                 swapped = True
    #         if not swapped:
    #             return A
    for i in range(len(A)//2):  # исправленный вариант
        for j in range(len(A) - 1 - i):  # не нужно от i in range(i, len(A) - 1 - i)
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a
        for j in range(len(A) - 2 - i, i + 1, -1):  # нужна еще -1 в конце in range(len(A) - 2 - i, i + 1)
            if A[j] < A[j - 1]:
                a = A[j]
                A[j] = A[j - 1]
                A[j - 1] = a


# 4. Функция сортировки выбором select:
def SelectSort(A):
    for i in range(len(A)):
        m = i
        for j in range(i, len(A)):
            if A[j] < A[m]:
                m = j
        A[i], A[m] = A[m], A[i]


# 5. Функция быстрой сортировки:
def QuickSort(A, fst, lst):  # быстрая сортировка
    if fst >= lst:
        return

    # i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst + 1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller - 1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время вставками", "Время шейкерной",
                                 "Время выбором", "Время быстрой"])

x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    B = A.copy()
    C = A.copy()
    D = A.copy()
    E = A.copy()

    # print(A)
    # BubbleSort(A)
    # print(A)

    # print("---")
    # print(B)
    # InsertSort(B)
    # print(B)

    # print("---")
    # print(C)
    # ShakerSort(C)
    # print(C)

    # print("---")
    # print(D)
    # SelectSort(D)
    # print(D)

    print("---")
    print("---")
    print("---")

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка" + str(N) + "заняла " + str((t2 - t1).total_seconds()) + "c")
    # print(A)

    t3 = datetime.datetime.now()
    InsertSort(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Сортировка вставками" + str(N) + "заняла " + str((t4 - t3).total_seconds()) + "c")
    # print(B)

    t5 = datetime.datetime.now()
    ShakerSort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Шейкерная сортировка" + str(N) + "заняла " + str((t6 - t5).total_seconds()) + "c")
    # print(C)

    t7 = datetime.datetime.now()
    SelectSort(D)
    t8 = datetime.datetime.now()
    y4.append((t8 - t7).total_seconds())
    print("Сортировка выбором" + str(N) + "заняла " + str((t8 - t7).total_seconds()) + "c")
    # print(D)

    t9 = datetime.datetime.now()
    QuickSort(E, 0, len(E) - 1)
    t10 = datetime.datetime.now()
    y5.append((t10 - t9).total_seconds())
    print("Быстрая сортировка" + str(N) + "заняла " + str((t10 - t9).total_seconds()) + "c")
    # print(E)

    table.add_row(
        [str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()), str((t6 - t5).total_seconds()),
         str((t8 - t7).total_seconds()), str((t10 - t9).total_seconds())])

print(table)

plt.plot(x, y1, "red")  # Пузырек
plt.plot(x, y2, "green")  # Вставками
plt.plot(x, y3, "yellow")   # Шейкерная
plt.plot(x, y4, "orange")  # Выбором
plt.plot(x, y5, "grey")   # Быстрая
plt.show()