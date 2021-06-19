def highest_pyramid(blocks):
    # Будем составлять словарь блоков, где ширина - ключ, а высота - значение.
    # Соответственно, в словаре будем хранить по 1 блоку с каждым значением ширины,
    # так как в пирамиде не может быть двух блоков одной ширины.
    # Будем запоминать только самый высокий блок
    blocks_dict = {}
    for w, h in blocks:
        if w in blocks_dict:
            if h > blocks_dict[w]:
                blocks_dict[w] = h
        else:
            blocks_dict[w] = h
    
    sum_h = 0
    for w in blocks_dict:
        sum_h += blocks_dict[w]
    return sum_h
    

n = int(input())
blocks = [list(map(int, input().split())) for i in range(n)]
print(highest_pyramid(blocks))