class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.parent = None

    def display_keys(self, space='\t', level=0):
        if self is None:
            print(space * level + '∅')
            return

        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        BSTNode.display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        BSTNode.display_keys(self.left, space, level + 1)

    def insert(self, key, value):
        if self is None:
            new_node = BSTNode(key, value)
            return new_node
        if self.key < key:
            self.right = BSTNode.insert(self.right, key, value)
            self.right.parent = self
        elif self.key > key:
            self.left = BSTNode.insert(self.left, key, value)
            self.left.parent = self
        return self

    def find(self, key):
        if self is None:
            return None
        if key == self.key:
            return self
        if key < self.key:
            return BSTNode.find(self.left, key)
        if key > self.key:
            return BSTNode.find(self.right, key)

    def update(self, key, value):
        target = BSTNode.find(self, key)
        if target is not None:
            target.value = value

    def list_all(self):
        if self is None:
            return []
        return BSTNode.list_all(self.left) + [(self.key, self.value)] + BSTNode.list_all(self.right)

    def is_balanced(self):
        if self is None:
            return True, 0
        balanced_l, height_l = BSTNode.is_balanced(self.left)
        balanced_r, height_r = BSTNode.is_balanced(self.right)
        balanced = balanced_r and balanced_l and abs(height_r - height_l) <= 1
        height = 1 + max(height_r, height_l)
        return balanced, height

    def balance_bst(self):
        return BSTNode.make_balanced_bst(BSTNode.list_all(self))

    def tree_height_max(self):
        if self is None:
            return 0
        return 1 + max(BSTNode.tree_height_max(self.left), BSTNode.tree_height_max(self.right))

    def __str__(self):
        return "BinaryTree <{}>".format(self.tree_to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.tree_to_tuple())

    def tree_to_tuple(self):
        if self is None:
            return None
        left_subtree = BSTNode.tree_to_tuple(self.left)
        right_subtree = BSTNode.tree_to_tuple(self.right)
        return left_subtree, self.key, right_subtree

    @staticmethod
    def remove_none(nums):
        return [x for x in nums if x is not None]

    @staticmethod
    def make_balanced_bst(data, lo=0, hi=None, parent=None):
        if hi is None:
            hi = len(data) - 1
        if lo > hi:
            return None

        mid = (lo + hi) // 2
        key, value = data[mid]
        root = BSTNode(key, value)
        root.parent = parent
        root.left = BSTNode.make_balanced_bst(data, lo, mid - 1, root)
        root.right = BSTNode.make_balanced_bst(data, mid + 1, hi, root)
        return root
