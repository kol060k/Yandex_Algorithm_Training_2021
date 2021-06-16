min_freq = 30.0
max_freq = 4000.0
n = int(input())
prev_freq = float(input())
for i in range(n-1):
    freq, word = input().split()
    freq = float(freq)
    if freq == prev_freq: # Если частоты равны, это измерение не даст никакой информации
        continue
    if word == 'closer':
        if freq < prev_freq:
            max_freq = min(max_freq, freq + (prev_freq-freq)/2)
        else:
            min_freq = max(min_freq, freq - (freq-prev_freq)/2)
    else:
        if freq < prev_freq:
            min_freq = max(min_freq, prev_freq - (prev_freq-freq)/2)
        else:
            max_freq = min(max_freq, prev_freq + (freq-prev_freq)/2)
    prev_freq = freq

print(min_freq, max_freq)