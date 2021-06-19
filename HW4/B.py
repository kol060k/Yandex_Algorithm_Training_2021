def word_appear(word_list):
    counts = {}
    for word in word_list:
        if word not in counts:
            counts[word] = 0
        else:
            counts[word] += 1
        print(counts[word], end=' ')


import sys
word_list = list(map(str, sys.stdin.read().split()))
word_appear(word_list)