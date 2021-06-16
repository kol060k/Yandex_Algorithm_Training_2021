n = int(input())
m = int(input())
union = set(input() for i in range(m))
intersection = union.copy()

for i in range(1,n):
    m = int(input())
    new_set = set(input() for i in range(m))
    union = union | new_set
    intersection = intersection & new_set

print(len(intersection))
for elem in intersection:
    print(elem)    
print(len(union))
for elem in union:
    print(elem)