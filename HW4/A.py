dict = {}
n = int(input())
for i in range(n):
    str1, str2 = list(map(str, input().split()))
    dict[str1] = str2
    dict[str2] = str1

word = input()
print(dict[word])