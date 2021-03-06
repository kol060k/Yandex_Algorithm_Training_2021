# Правильная расстановка охранников, согласно условию, есть такая, что их время дежурства строго
# следуют друг за другом, может быть пересекаясь концами (начало одного и конец другого, причём
# должны быть моменты, когда каждый охранник дежурит один, чтобы его нельзя было удалить):
# (.....]
#     (.....]
#         (......]
#              (.....]
# Храним начала и концы дежурств охранников в формате (start, stop], как в условии,
# type_start = -1, type_end = 1 (хотя они и происходят в другой пос-ти, но так удобнее для алгоритма).
# Тогда отсортированная последовательность событий должна выглядеть так:
# 1) start первого охранника ровно в 0, а у следующего строго позже
# 2) start и stop охранников строго чередуются (кроме ситуации с первым охранником), причём
#    stop дерурства должен приходиться всегда на охранника, который заступил раньше из двух работающих
#    в текущий момент. Причём start и stop могут быть одновременно, в силу того, что type_start < type_end,
#    start в списке событий расположится раньше, хотя по смыслу новый охранник заступит сразу после старого,
#    главное, что даже такой случай не ломает пункт 2)
# 3) end последнего охранника должен быть в момент 10000, а предпоследнего строго меньше 10000

def chech_security(test):
    n = test[0]
    type_start = -1
    type_end = 1
    events = []
    for i in range(n):
        events.append((test[2*i+1], type_start, i))
        events.append((test[2*i+2], type_end, i))
    events.sort()
    if len(events) == 2:
        # Если охранник только один, рассматриваем отдельно
        if events[0][0] != 0 and events[1][0] != 10000:
            return False
    else:
        # условие 1
        if events[0][0] != 0 or events[1][0] == 0:
            return False
        if events[1][1] != type_start:
            return False
        # условие 3
        if events[2*n-1][0] != 10000 or events[2*n-2][0] == 10000:
            return False
        # условие 2
        # Пробегаемся по всем событиям кроме первых двух и последнего (их мы проверили в условиях 1 и 3)
        old_security = events[0][2] # тут хранится номер охранника, который заступил раньше из двух работающих
        new_security = events[1][2] # тут будет храниться охранник, который заступил позже
        for i in range(2, 2*n-1):
            if events[i][1] == events[i-1][1]:
                return False
            if events[i][1] == type_end:
                if events[i][2] == old_security:
                    old_security = new_security
                else:
                    return False
            elif events[i][1] == type_start:
                new_security = events[i][2]
    return True
    
    
k = int(input())
for i in range(k):
    test = list(map(int, input().split()))
    if chech_security(test):
        print('Accepted')
    else:
        print('Wrong Answer')