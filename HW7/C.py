def share_variants(n, d, students):
    # Будем решать задачу просто двумя указателями, находя максимальное количество студентов,
    # которые могут находиться на отрезке [x, x+d] для всех x
    # Дипломы раздадим на втором проходе просто по очереди: 1, 2, 3, 4, 1, 2, 3, 4, 1,...
    # так точно будет правильно
    students_sorted = sorted([(students[i], i) for i in range(n)])
    variants_need = 0
    R = 0
    for L in range(n):
        while R < n and (R == L or students_sorted[R][0] - students_sorted[L][0] <= d):
            R += 1
        variants_need = max(variants_need, R - L)
    ans = [0] * n
    for i in range(n):
        ans[students_sorted[i][1]] = i % variants_need + 1
    return variants_need, ans
    

n, d = map(int, input().split())
students = list(map(int, input().split()))
variants, ans = share_variants(n, d, students)
print(variants)
print(*ans)