class Node:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.value = n


def tree_by_levels(node):
    if node is None:
        return []
    queue = [node]
    visited = []
    while queue:
        current_node = queue.pop(0)
        visited.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    return visited


tree = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)
print(tree_by_levels(tree))
