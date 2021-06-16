arr = list(map(int, input().split()))
pos1 = 0
pos2 = 0
neg1 = 0
neg2 = 0
zeros_num = 0
for num in arr:
    if num > 0:
        if num > pos1:
            pos2 = pos1
            pos1 = num
        elif num > pos2:
            pos2 = num
    elif num < 0:
        if num < neg1:
            neg2 = neg1
            neg1 = num
        elif num < neg2:
            neg2 = num
    else:
        zeros_num += 1
if pos2 > 0:
    if pos1 * pos2 > neg1 * neg2:
        print(pos2, pos1)
    else:
        print(neg1, neg2)
elif neg2 < 0:
    print(neg1, neg2)
elif zeros_num > 0:
    if pos1 > 0:
        print(0, pos1)
    elif neg1 < 0:
        print(neg1, 0)
    else:
        print(0, 0)
else:
    print(neg1, pos1)