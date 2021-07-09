def create_tree(key):
    root = {'key': key, 'left': None, 'right': None, 'up': None, 'height': 1}
    return root


def add_node(root, key):
    if key < root['key']:
        if root['left'] is not None:
            new_height = add_node(root['left'], key)
            root['height'] = max(root['height'], new_height + 1)
        else:
            root['left'] = {'key': key, 'left': None, 'right': None, 'up': root, 'height': 1}
            root['height'] = max(root['height'], 2)
    elif key > root['key']:
        if root['right'] is not None:
            new_height = add_node(root['right'], key)
            root['height'] = max(root['height'], new_height + 1)
        else:
            root['right'] = {'key': key, 'left': None, 'right': None, 'up': root, 'height': 1}
            root['height'] = max(root['height'], 2)
    return root['height']


def check_AVL(root):
    if root['left'] is not None and root['right'] is not None:
        if abs(root['left']['height'] - root['right']['height']) > 1:
            return False
        return check_AVL(root['left']) and check_AVL(root['right'])
    elif root['left'] is not None:
        if root['left']['height'] > 1:
            return False
    elif root['right'] is not None:
        if root['right']['height'] > 1:
            return False
    return True


numbers = list(map(int, input().split()))
tree = create_tree(numbers[0])
for i in range(1, len(numbers)-1):
    add_node(tree, numbers[i])
if check_AVL(tree):
    print('YES')
else:
    print('NO')