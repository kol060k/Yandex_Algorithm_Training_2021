def points_in_segments(n, m, starts, ends, points):
    start_type = -1
    end_type = 1
    point_type = 0
    events = [0] * (n * 2 + m)
    for i in range(n):
        # В задаче есть хитрость! Иногда start > end - отрезок перевёрнут, нужно правильно присвоить тип
        events[2*i] = (starts[i], start_type if starts[i] < ends[i] else end_type)
        events[2*i + 1] = (ends[i], end_type if starts[i] < ends[i] else start_type)
    for i in range(m):
        # Также для каждой точки сохраним её номер, чтобы затем вывести в правильном порядке
        events[2*n + i] = (points[i], point_type, i)
    events.sort()
    cur_segments = 0
    ans = [0] * m
    for event in events:
        if event[1] == start_type:
            cur_segments += 1
        elif event[1] == end_type:
            cur_segments -= 1
        else:
            ans[event[2]] = cur_segments
    return ans
    

n, m = map(int, input().split())
starts = [0] * n
ends = [0] * n
for i in range(n):
    starts[i], ends[i] = map(int, input().split())
points = list(map(int, input().split()))
 
ans = points_in_segments(n, m, starts, ends, points)
print(*ans)