def cards_prepare(cards):
    '''
    Собрать словарь, содержащий кол-во раз, сколько встретилась каждая карта
    и отсортированный список этих карт (уникальные карты)
    '''
    card_dict = {}
    for card in cards:
        if card not in card_dict:
            card_dict[card] = 0
        card_dict[card] += 1
    uniq_cards = sorted(card for card in card_dict)
    return card_dict, uniq_cards


def calc_aaa(card_dict):
    '''
    Вычисляем кол-во вариантов взять 3 одинаковые карты
    '''
    cnt = 0
    for card in card_dict:
        if card_dict[card] >= 3:
            cnt += 1
    return cnt


def calc_aab(card_dict, uniq_cards, k):
    '''
    Вычисляем кол-во вариантов заполнить табло карточками вида a:a:b или любая перестановка
    Пусть b > a, тогда мы считаем все варианты вида a:a:b и a:b:b (и их перестановки)
    '''
    cnt = 0
    num_doubles = 0 # Кол-во карточек в количестве хотя бы 2 на интервале [L, R)
    R = 0
    for L in range(len(uniq_cards)):
        while R < len(uniq_cards) and (R == L or uniq_cards[R] <= uniq_cards[L] * k):
            cnt += num_doubles # a:a:b
            if card_dict[uniq_cards[R]] >= 2:
                cnt += (R - L) # a:b:b
                num_doubles += 1
            R += 1
        if card_dict[uniq_cards[L]] >= 2:
            num_doubles -= 1
    return cnt * 3 # Умножение на 3, так как счёт вида a:a:b имеет ровно 3 перестановки


def calc_abc(uniq_cards, k):
    '''
    Вычисляем кол-во вариантов заполнить табло счётом вида a:b:c, где все 3 карты разные
    '''
    cnt = 0
    R = 1
    for L in range(len(uniq_cards)):
        while R < len(uniq_cards) and (R <= L + 1 or uniq_cards[R] <= uniq_cards[L] * k):
            cnt += (R - L) * (R - L - 1) // 2
            R += 1
    return cnt * 6 # Умножение на 6, так как счёт вида a:b:c имеет ровно 6 перестановок
        
    
n, k = map(int, input().split())
cards = list(map(int, input().split()))
card_dict, uniq_cards = cards_prepare(cards)
print(calc_aaa(card_dict) + calc_aab(card_dict, uniq_cards, k) + calc_abc(uniq_cards, k))