arr = list(map(int, input().split()))
pos1 = 0
pos2 = 0
pos3 = 0
neg1 = 0
neg2 = 0
zeros_num = 0
for num in arr:
    if num > 0:
        if num > pos1:
            pos3 = pos2
            pos2 = pos1
            pos1 = num
        elif num > pos2:
            pos3 = pos2
            pos2 = num
        elif num > pos3:
            pos3 = num
    elif num < 0:
        if num < neg1:
            neg2 = neg1
            neg1 = num
        elif num < neg2:
            neg2 = num
    else:
        zeros_num += 1

if pos3 > 0:
    if pos1 * pos2 * pos3 > pos1 * neg1 * neg2:
        print(pos1, pos2, pos3)
    else:
        print(pos1, neg1, neg2)
elif pos1 > 0 and neg2 < 0:
    print(pos1, neg1, neg2)
elif zeros_num > 0:
    if zeros_num >= 3:
        print(0, 0, 0)
    elif zeros_num == 2:
        if pos1 > 0:
            print(0, 0, pos1)
        else:
            print(0, 0, neg1)
    else:
        if pos2 > 0:
            print(0, pos1, pos2)
        elif neg2 < 0:
            print(0, neg1, neg2)
        else:
            print(0, pos1, neg1)
else:
    if pos2 > 0:
        print(pos1, pos2, neg1)
    else: # Придётся искать 3 самых маленьких по модулю отрицательных числа
        neg1 = 0
        neg2 = 0
        neg3 = 0
        for num in arr:
            if neg1 == 0 or num > neg1:
                neg3 = neg2
                neg2 = neg1
                neg1 = num
            elif neg2 == 0 or num > neg2:
                neg3 = neg2
                neg2 = num
            elif neg3 == 0 or num > neg3:
                neg3 = num
        print(neg1, neg2, neg3)