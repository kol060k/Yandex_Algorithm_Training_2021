str1 = input()
str2 = input()

pair_set = set(''.join([str2[i], str2[i+1]]) for i in range(len(str2) - 1))

k = 0
for i in range(len(str1) - 1):
    if ''.join([str1[i], str1[i+1]]) in pair_set:
        k += 1

print(k)