def check_keyboard(durability, taps):
    for tap in taps:
        durability[tap - 1] -= 1

    for button in durability:
        if button < 0:
            print('YES')
        else:
            print('NO')


n = int(input())
durability = list(map(int, input().split()))
k = int(input())
taps = list(map(int, input().split()))

check_keyboard(durability, taps)