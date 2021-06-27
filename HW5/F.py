def calc_price(classes, conds):
    price = 0
    L = 1 # conds индексируется с [1]
    for cls_pow in classes:
        # Для каждого класса ищем наиболее дешёвый кондиционер подходящей мощности (power >= cls_pow)
        # Массив classes упорядочен, так что для каждого нового класса не нужно пробегать массив conds заново
        while(conds[L] < cls_pow):
            L += 1
        price += L
    return price

    
n = int(input())
classes = sorted(list(map(int, input().split())))
m = int(input())
conds = [0] * 1001 # Массив для хранения самых мощных кондиционеров для каждой стоимости
# Делаем именно в таком виде, так как более мощные кондиционеры могут быть дешевле, нам это подходит
# Индексируем массив от [1] до [1000]
for i in range(m):
    power, price = map(int, input().split())
    conds[price] = max(conds[price], power)

print(calc_price(classes, conds))