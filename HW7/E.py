# Определим время работы всех касс на протяжении суток в два прохода по дню.
# Будем поддерживать сет открытых касс и начнём пробегаться по дню с 00:00.
# Если встречается событие закрытия кассы, которая ещё не открыта, значит она работает в полночь,
# дойдём до её открытия к концу дня, а пока ничего не делаем. Если встречается закрытие открытой кассы,
# то штатно удаляем кассу из сета. Итого к концу первого дня у нас составится релевантный список
# открытых касс на момент полночи, и тогда с нового дня мы будем совершать правильный пробег по кассам.
#
# На втором пробеге по кассам будем смотреть, когда количество открытых касс равно n и запоминать время.
# Можно сделать проще: перед каждым закрытием кассы проверяем, не было ли до этого открыто n касс.
# Если все кассы были открыты, то открыты они были ровно время между мекущим и предыдущим событием.
# Действительно, предыдущее событие не могло быть закрытием, так как были открыты все кассы, значит
# предыдущее событие было открытием, а значит до него были открыты не все кассы, то есть время работы всех
# касс есть ровно время до предыдущего события.
# Отдельно только стоит расписать случай, когда в полночь уже открыты все кассы.
#
# type_open = 1, а type_close = -1 для правильной сортировки кассы, так как касса закрывается раньше, чем
# открывается новая с тем же временем в силу невключительности времени закрытия во временной отрезок.

def all_windows_open(n, t_close, t_open):
    type_open = 1
    type_close = -1
    events = []
    for i in range(n):
        events.append((t_open[i], type_open, i))
        events.append((t_close[i], type_close, i))
    events.sort()
    opened_windows = set()
    # Первый пробег:
    for event in events:
        if event[1] == type_open:
            opened_windows.add(event[2])
        elif event[2] in opened_windows:
            opened_windows.remove(event[2])
    # Отдельно обрабатываем случай, когда в полночь открыты все кассы и первое событие после полночи:
    all_opened_time = 0
    if len(opened_windows) == n:
        all_opened_time += 24 * 60 + events[0][0] - events[2*n-1][0]
    if events[0][1] == type_open:
        opened_windows.add(events[0][2])
    else:
        opened_windows.remove(events[0][2])
    # Второй проход без первого события, которое мы обработали отдельно
    for i in range(1, len(events)):
        if events[i][1] == type_open:
            opened_windows.add(events[i][2])
        else:
            if len(opened_windows) == n:
                all_opened_time += events[i][0] - events[i-1][0]
            opened_windows.remove(events[i][2])
    return all_opened_time
        
    
n = int(input())
t_open = [0] * n
t_close = [0] * n
for i in range(n):
    open_h, open_m, close_h, close_m = map(int, input().split())
    t_open[i] = open_h * 60 + open_m
    t_close[i] = close_h * 60 + close_m
print(all_windows_open(n, t_close, t_open))