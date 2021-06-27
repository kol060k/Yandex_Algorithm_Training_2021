def calc_variants(string, k):
    cnt = 0
    R = k  # [L, R)
    for L in range(len(string)):
        # Находим подпос-ть максимальной длины k+m, что str[i] = str[i+k] для i in range(m)
        # В такой подпос-ти можно выбрать m*(m+1)/2 способов выборать эффективный режим работы робота:
        # если загрузить в память команды str[0:k], то остановить робота можно на любой из m операций str[k:k+m]
        # если загрузить команды str[1:k+1], то остановить можно на любой из m-1 операций str[k+1:k+m]
        # и т. д.
        while R < len(string) and (R < L + k or string[R] == string[R-k]):
            R += 1
            cnt += R - L - k # Прибавление этих величин при каждом увеличении R аналогично тому, что описано выше
    return cnt

k = int(input())
string = input()
print(calc_variants(string, k))