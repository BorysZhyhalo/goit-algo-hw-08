"""
Завдання 1

Напишіть алгоритм (функцію), який знаходить найменше значення у двійковому дереві пошуку або в AVL-дереві. 
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

"""

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    """Вставка в BST."""
    if root is None:
        return BSTNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    return root


def find_min_value(root):
    """
    Найменше значення в BST/AVL.
    Час: O(h), пам'ять: O(1).
    """
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current.key

def main():
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)

    print("Мінімум після вставок:", find_min_value(root)) 
    print("Мінімум у поточному дереві:", find_min_value(root))


if __name__ == "__main__":
    main()
    
