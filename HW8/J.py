children = {} # словарь, возвращающий детей человека
parent = {} # словарь, возвращающий родителя человека
n = int(input())
# Заполняем оба словаря:
for i in range(n-1):
    child_name, parent_name = input().split()
    parent[child_name] = parent_name
    if parent_name not in children:
        children[parent_name] = []
    children[parent_name].append(child_name)
    
# Найдём прародителя, у него должны быть дети, но при этом не должно быть родителя
TheGodfather = set(children.keys()) - set(parent.keys())
TheGodfather = list(TheGodfather)[0] # Он всё равно один

# Пройдём по всем людям сверху вниз (от родителей к детям) и с каждым спуском будем увеличивать
# уровень на один. Это алгоритм поиска в ширину с начала дерева.
# Для начала составим очередь от самого старого.
queue = [TheGodfather]
i = 0
while i < len(queue):
    if queue[i] in children:
        queue.extend(children[queue[i]])
    i += 1
# Теперь проходимся по очереди от родителей к детям и записываем число потомков
level = {}
level[TheGodfather] = 0
for i in range(1, len(queue)):
    level[queue[i]] = level[parent[queue[i]]] + 1

# Выводим в лексикографическом порядке
for person in sorted(level.keys()):
    print(person, level[person])