import sys

def read_key_words(n, reg_sense):
    # Считываем все ключевые слова. Если регистр не важен, сразу же заменим все буквы на маленькие.
    if reg_sense == 'yes':
        key_words = set([input() for i in range(n)])
    else:
        key_words = set([input().lower() for i in range(n)])
    return key_words


def analyse_code(reg_sense, num_start, key_words):
    # Считываем код программы. Если регистр не важен, сразу же заменим все буквы на маленькие.
    if reg_sense == 'yes':
        code = sys.stdin.read()
    else:
        code = sys.stdin.read().lower()
    
    # Выбросим лишние символы и заменим их на пробелы (так как "лишние" символы являются разделителями идентификаторов)
    code_symbols = []
    for c in code:
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c == '_') or (c >= '0' and c <= '9'):
            code_symbols.append(c);
        else:
            code_symbols.append(' ')
    code = ''.join(code_symbols)
    
    # Теперь можно разделить остаток кода на слова - кандидаты на идентификаторы
    code = code.split()
    
    # Подсчитаем частоту, с которой встречаются идентификаторы
    id_count = {}
    for word in code:
        if word not in key_words:
            if (num_start == 'yes' or (word[0] < '0' or word[0] > '9')) and not word.isdigit():
                if word not in id_count:
                    id_count[word] = 0
                id_count[word] += 1
    
    # Теперь находим те идентификаторы, которые встречались чаще всего
    max_count = 0
    for word in id_count:
        if id_count[word] > max_count:
            max_count = id_count[word]
    most_frequent = [word for word in id_count if id_count[word] == max_count]
    
    # Находим первый встречающийся самый частый идентификатор. Это и есть ответ
    for word in code:
        if word in most_frequent:
            return word

    
n, reg_sense, num_start = input().split()
n = int(n)
key_words = read_key_words(n, reg_sense)
answer = analyse_code(reg_sense, num_start, key_words)
print(answer)