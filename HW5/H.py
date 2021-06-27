def longest_substring(string, k):
    symbols = [0] * 26 # 26 счётчиков для каждой буквы в строке (состоит из 'a' - 'z')
    longest = 0
    longest_start = 0
    L = 0
    R = 0
    more_than_k_symb = 0 # Символ, который встречается более k раз в [L, R)
    # Пока не дошли до конца правым указателем и пока в конце не будет шанса найти более длинную подстроку:
    while R < len(string):
        if more_than_k_symb == 0: # Если подстрока подходит, сдвигаем её правый конец
            symbols[ord(string[R]) - ord('a')] += 1
            if symbols[ord(string[R]) - ord('a')] > k:
                more_than_k_symb = ord(string[R])
            else:
                if R - L >= longest:
                    longest = R - L + 1
                    longest_start = L
            R += 1
        else: # Есди есть какой-то символ, который встречается более k раз, двигаем левый конец
            symbols[ord(string[L]) - ord('a')] -= 1
            if symbols[more_than_k_symb - ord('a')] <= k:
                more_than_k_symb = 0
            L += 1
                # Проверка на самую длинную строку не нужна, т.к. подходящая строка такой же длины точно уже была
    return longest, longest_start + 1


n, k = map(int, input().split())
string = input()
answer = longest_substring(string, k)
print(answer[0], answer[1])