def rectangle(a, b, n=0):
    if a == b:
        return n + 1
    elif a < b:
        return rectangle(a, b - a, n + 1)
    return rectangle(a - b, b, n + 1)

a = int(input("Сторона а=\n"))
b = int(input("Сторона b=\n"))

print(f"Прямоугольнику с длинами {a} и {b} можно нарезать {rectangle(a, b)} квадратов")