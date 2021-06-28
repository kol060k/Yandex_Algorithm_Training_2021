def bin_search(source_arr, elem_arr):
    for elem in elem_arr:
        L = 0
        R = len(source_arr) - 1
        while L < R:
            m = (L + R) // 2
            if (source_arr[m] < elem):
                L = m + 1
            else:
                R = m
        if (source_arr[L] == elem):
            print('YES')
        else:
            print('NO')
            

n, k = map(int, input().split())
source_arr = list(map(int, input().split()))
elem_arr = list(map(int, input().split()))
bin_search(source_arr, elem_arr)