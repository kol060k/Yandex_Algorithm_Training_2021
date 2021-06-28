def is_enough(a, b, c, num_5):
    # Функция считает среднюю оценку и сравнивает с 4
    # Вместо деления будем производить умножение (без потери точности)
    return a * 2 + b * 3 + c * 4 + num_5 * 5 >= 3.5 * (a + b + c + num_5)


def min_excellent(a, b, c):
    # Будем перебирать количество пятёрок от 0 до a+b+c
    # (точно хватит, так как одна пятёрка "уравновешивает" двойку)
    L = 0
    R = a + b + c
    while L < R:
        m = (L + R) // 2
        if is_enough(a, b, c, m):
            R = m
        else:
            L = m + 1
    return L
    

a = int(input())
b = int(input())
c = int(input())
print(min_excellent(a, b, c))