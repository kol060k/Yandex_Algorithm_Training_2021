def is_enough_segments(n, k, L_arr, length):
    # Посчитаем, сколько отрезков длины length можно получить порезав наш набор L
    max_segments = sum([L_i // length for L_i in L_arr])
    return max_segments >= k


def max_segment_len(n, k, L_arr):
    # Макс. возможная длина отрезков - 10 000 000, так как все L_i <= 10 000 000
    L = 0
    R = 10000000
    while L < R:
        m = (L + R + 1) // 2
        if is_enough_segments(n, k, L_arr, m):
            L = m
        else:
            R = m - 1
    return L
    

n, k = map(int,input().split())
L_arr = [int(input()) for i in range(n)]
print(max_segment_len(n, k, L_arr))