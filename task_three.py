def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Перемістити диск з {source} на {target}: {n}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Перемістити диск з {source} на {target}: {n}")
    hanoi(n - 1, auxiliary, target, source)

# Виклик функції для 3 дисків
n = 4
hanoi(n, 'A', 'C', 'B')
