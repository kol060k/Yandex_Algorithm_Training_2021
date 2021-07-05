def cheating_stidents(n, m, starts, ends):
    start_type = -1
    end_type = 1
    events = [0] * m * 2
    for i in range(m):
        events[2*i] = (starts[i], start_type)
        events[2*i + 1] = (ends[i], end_type)
    events.sort()
    not_cheating = 0 # посчитаем тех, кто не списывает, а затем вычтем из N (так проще)
    num_observers = 0
    for i in range(len(events)):
        if num_observers == 0:
            # если наблюдателей не было, значит текущее событие - точно start
            not_cheating += 1
        else:
            # если наблюдатели были, значит предыдущие люди точно под присмотром
            not_cheating += events[i][0] - events[i-1][0]
        if events[i][1] == start_type:
            num_observers += 1
        else:
            num_observers -= 1
    return n - not_cheating
    

n, m = map(int, input().split())
starts = [0] * m
ends = [0] * m
for i in range(m):
    starts[i], ends[i] = map(int, input().split())
print(cheating_stidents(n, m, starts, ends))