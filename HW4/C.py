def most_freq_word(word_list):
    counts = {}
    for word in word_list:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    max_count = 0
    for word in counts:
        if counts[word] > max_count:
            max_count = counts[word]
            best_word = word
        elif counts[word] == max_count:
            if word < best_word:
                best_word = word
    print(best_word)


import sys
word_list = list(map(str, sys.stdin.read().split()))
most_freq_word(word_list)