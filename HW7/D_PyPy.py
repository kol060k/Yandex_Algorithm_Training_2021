# Разумно ставить рекламу в моменты, когда что-то происходит. Этим событием может быть
# либо приход человека, либо его уход, но если это уход, то располагаем ролик за 5 минут до его ухода,
# чтобы человек имел возможность посмотреть его.
# Далее для удобства работы с отрезками, сократим абсолютно все отрезки на 5 ед. времени.
# В таком случае ролики станут точечными, а мы будем ставить их либо во время прихода, либо
# во время ухода покупателя. Времена посещения покупателей тоже станут на 5 ед. времени короче с конца.
# Тех, кто бы в магазине менее 5 ед. времени, мы вообще не рассматриваем (они и ранее не играли роли).
#
# Теперь, когда события показа ролика точечные, нам достаточно просто запомнить всех людей, которые были
# в магазине на момент его показа. Будем перебирать все пары постановки рекламных роликов и искать лучшую.

def place_ad(n, t_come, t_leave, ad_len = 5):
    come_type = -1
    leave_type = 1
    events = []
    for i in range(n):
        if t_leave[i] - t_come[i] >= 5:
            events.append((t_come[i], come_type, i))
            events.append((t_leave[i]  - 5, leave_type, i))
    events.sort()
    # Отдельно обрабатываем случай 0 и 1 оставшихся покупателей:
    if len(events) == 0:
        return (0, 1, 6)
    if len(events) == 2:
        return (1, events[0][0], events[0][0] + 5)
    best_watched = 0
    first_watched = set() # Люди, которые посмотрели первый ролик
    for i in range(len(events)):
        # Обрабатываем событие и параллельно вставляем первую рекламу. 
        # Приоритет одновременных событий: приход, реклама, уход
        if events[i][1] == come_type:
            first_watched.add(events[i][2])
            if len(first_watched) > best_watched:
                # Обработка случая, когда единсвенная реклама уже лучшая на текущий момент
                # Это рассматривается отдельно на случай, если первый ролик поставлен где-то в конце дня
                # и второй ролик просто не удаётся вставить с интервалом в 5 ед. времени.
                best_watched = len(first_watched)
                firstad = events[i][0]
                secondad = events[i][0] + 5
        second_watched = 0 # Кол-во людей, посмотревших 2-й ролик и не посмотревших 1-й
        for j in range(i + 1, len(events)):
            # Аналогично проверяем все возможности вставить вторую рекламу
            if events[j][1] == come_type and events[j][2] not in first_watched:
                second_watched += 1
            if events[j][0] - events[i][0] >= 5 and second_watched + len(first_watched) > best_watched:
                best_watched = len(first_watched) + second_watched
                firstad = events[i][0]
                secondad = events[j][0]
            if events[j][1] == leave_type and events[j][2] not in first_watched:
                second_watched -= 1
        if events[i][1] == leave_type:
            first_watched.remove(events[i][2])
    return (best_watched, firstad, secondad)

        
n = int(input())
comings = [0] * n
leaves = [0] * n
for i in range(n):
    comings[i], leaves[i] = map(int, input().split())
print(*place_ad(n, comings, leaves))