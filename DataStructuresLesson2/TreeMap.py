from BSTNode import BSTNode


class TreeMap:
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = BSTNode.find(self.root, key)
        if not node:
            self.root = BSTNode.insert(self.root, key, value)
            self.root = BSTNode.balance_bst(self.root)
        else:
            BSTNode.update(self.root, key, value)

    def __getitem__(self, key):
        node = BSTNode.find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in BSTNode.list_all(self.root))

    def __len__(self):
        return BSTNode.tree_height_max(self.root)

    def display(self):
        return BSTNode.display_keys(self.root)
