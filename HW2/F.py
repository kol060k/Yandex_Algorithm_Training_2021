n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    palindrome = True
    for j in range((n-i) // 2):
        if arr[i+j] != arr[n-1-j]:
            palindrome = False
            break
    if palindrome:
        print(i)
        if i > 0:
            for j in range(i-1, -1, -1):
                print(arr[j], end=' ')
        break