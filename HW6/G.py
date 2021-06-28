def is_enough_tile(n, m, t, w):
    # Считаем количество плитки для построения дорожки шириной w и сравниваем с имеющимся
    # Модуль в выражении ниже взят для того, чтобы ширина дороги больше, чем половина площади
    # автоматически была неподходящим вариантом
    tiles_need = n * w * 2 + abs(m - 2 * w) * w * 2
    return tiles_need <= t


def max_road_w(n, m, t):
    # Макс. возможная ширина дороги точно меньше min(m, n)
    L = 0
    R = min(m, n)
    while L < R:
        w = (L + R + 1) // 2
        if is_enough_tile(n, m ,t, w):
            L = w
        else:
            R = w - 1
    return L
    

n = int(input())
m = int(input())
t = int(input())
print(max_road_w(n, m, t))