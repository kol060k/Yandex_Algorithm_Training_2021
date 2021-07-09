def create_tree(key):
    root = {'key': key, 'left': None, 'right': None, 'up': None, 'depth': 1}
    return root


def add_node(root, key):
    if key < root['key']:
        if root['left'] is not None:
            new_depth = add_node(root['left'], key)
        else:
            root['left'] = {'key': key, 'left': None, 'right': None, 'up': root, 'depth': root['depth'] + 1}
            new_depth = root['depth'] + 1
    elif key > root['key']:
        if root['right'] is not None:
            new_depth = add_node(root['right'], key)
        else:
            root['right'] = {'key': key, 'left': None, 'right': None, 'up': root, 'depth': root['depth'] + 1}
            new_depth = root['depth'] + 1
    else: # key == root['key']
        new_depth = None
    return new_depth


def greatest_elem(root):
    if root['right'] is not None:
        ans = greatest_elem(root['right'])
    else:
        ans = root
    return ans


def second_greatest_key(root):
    # Второй по величине элемент в дереве - это либо наибольший элемент в левом дереве от
    # наибольшего элемента, если оно есть, либо есть нет, то родитель наибольшего элемента
    # (нам гарантируется, что второй наибольший точно есть).
    greatest = greatest_elem(root)
    if greatest['left'] is not None:
        second_greatest = greatest_elem(greatest['left'])
    else:
        second_greatest = greatest['up']
    return second_greatest['key']


numbers = list(map(int, input().split()))
tree = create_tree(numbers[0])
for i in range(1, len(numbers)-1):
    add_node(tree, numbers[i])
print(second_greatest_key(tree))