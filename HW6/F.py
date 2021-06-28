def is_enough_time(n, x, y, time):
    # Функция считает, хватит ли времени на распечатку n копий.
    # Сначала делаем 1 копию на самом быстром сканере,
    # а затем копируем имеющиеся две параллельно на обоих сканерах
    first_copy_time = min(x, y) # время создания первой копии
    x_max = (time - first_copy_time) // x # Макс. число копий за оставшееся время
    y_max = (time - first_copy_time) // y
    total_copies = x_max + y_max + 1
    return total_copies >= n


def min_time_binsearch(n, x, y):
    # (x + y) * n времени точно хватит - это будет правой границей
    L = 0
    R = n * (x + y)
    while L < R:
        m = (L + R) // 2
        if is_enough_time(n, x, y, m):
            R = m
        else:
            L = m + 1
    return L
    

n, x, y = map(int, input().split())
print(min_time_binsearch(n, x, y))