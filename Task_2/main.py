"""
Завдання 2
Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві. 
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

"""

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root


def find_tree_sum(root):
    if root is None:
        return 0
    return root.key + find_tree_sum(root.left) + find_tree_sum(root.right)


def main():
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)

    print("Сума всіх значень:", find_tree_sum(root))
    


if __name__ == "__main__":
    main()