def is_fit(w, h, n, size):
    # Функция проверяет, влезут ли дипломы на доску size x size
    w_max = size // w
    h_max = size // h
    return w_max * h_max >= n

def smallest_desk(w, h, n):
    # Будем перебирать размеры доски от 1 до max(n*w, h) (если все дипломы повесить в один ряд)
    L = 1
    R = max(n * w, h)
    while L < R:
        m = (L + R) // 2
        if is_fit(w, h, n, m):
            R = m
        else:
            L = m + 1
    return L


w, h, n = map(int, input().split())
print(smallest_desk(w, h, n))