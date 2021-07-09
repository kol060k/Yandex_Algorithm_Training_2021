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


numbers = list(map(int, input().split()))
tree = create_tree(numbers[0])
depths = [1]
for i in range(1, len(numbers)-1):
    cur_depth = add_node(tree, numbers[i])
    if cur_depth is not None:
        depths.append(cur_depth)
print(*depths)