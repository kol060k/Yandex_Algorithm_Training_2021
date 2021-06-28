def bin_closest_search(source_arr, elem_arr):
    for elem in elem_arr:
        L = 0
        R = len(source_arr) - 1
        while L < R - 1:
            # Будем сходиться не до 1 числа, а до двух, чтобы первое было меньше искомого, а второе больше
            # Тогда если число, равное elem не найдётся, то посмотрим, какое из двух оставшихся ближе к искомому
            m = (L + R) // 2
            if source_arr[m] > elem:
                R = m
            else:
                L = m
        if elem - source_arr[L] <= source_arr[R] - elem:
            print(source_arr[L])
        else:
            print(source_arr[R])


n, k = map(int, input().split())
source_arr = list(map(int, input().split()))
elem_arr = list(map(int, input().split()))
bin_closest_search(source_arr, elem_arr)