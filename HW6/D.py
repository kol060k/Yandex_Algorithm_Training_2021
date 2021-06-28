def is_fit(n, a, b, w, h, armor):
    # Функция проверяет, влезут ли дипломы на доску size x size
    w_max = w // (a + 2 * armor)
    h_max = h // (b + 2 * armor)
    return w_max * h_max >= n


def max_armor(n, a, b, w, h):
    # Будем перебирать размеры защиты от 0 до max(w, h)
    L = 0
    R = max(w, h)
    while L < R:
        m = (L + R + 1) // 2
        if is_fit(n, a, b, w, h, m):
            L = m
        else:
            R = m - 1
    return L
    

n, a, b, w, h = map(int, input().split())
# Рассчитаем максимальный размер защиты при обоих ориентациях жилых блоков и выберем наибольший
print(max(max_armor(n, a, b, w, h), max_armor(n, a, b, h, w)))