arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))
for elem in arr1:
    if elem in arr2:
        print(elem, end=' ')