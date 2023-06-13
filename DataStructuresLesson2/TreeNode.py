class TreeNode:
    def __init__(self, key=None):
        self.key = key
        self.right = None
        self.left = None

    def tree_to_tuple(self):
        if self is None:
            return None
        left_subtree = TreeNode.tree_to_tuple(self.left)
        right_subtree = TreeNode.tree_to_tuple(self.right)
        return left_subtree, self.key, right_subtree

    def display_keys(self, space='\t', level=0):
        if self is None:
            print(space * level + '∅')
            return

        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        TreeNode.display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        TreeNode.display_keys(self.left, space, level + 1)

    def inordertraversal(self):
        if self is None:
            return []
        return TreeNode.inordertraversal(self.left) + [self.key] + TreeNode.inordertraversal(self.right)

    def preordertraversal(self):
        if self is None:
            return []
        return [self.key] + TreeNode.preordertraversal(self.left) + TreeNode.preordertraversal(self.right)

    def postordertraversal(self):
        if self is None:
            return []
        return TreeNode.postordertraversal(self.left) + TreeNode.postordertraversal(self.right) + [self.key]

    def tree_height_max(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.tree_height_max(self.left), TreeNode.tree_height_max(self.right))

    def tree_height_min(self):
        if self is None:
            return 0
        queue = [(self, 1)]
        while queue:
            node, depth = queue.pop(0)
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])
        return -1

    def tree_diameter(self):
        diameter = 0

        def get_height(node):
            if node is None:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)
            nonlocal diameter
            diameter = max(diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        get_height(self)
        return diameter

    def __str__(self):
        return "BinaryTree <{}>".format(self.tree_to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.tree_to_tuple())

    def is_bst(self):
        if self is None:
            return True, None, None

        is_bst_l, min_l, max_l = TreeNode.is_bst(self.left)
        is_bst_r, min_r, max_r = TreeNode.is_bst(self.right)

        is_bst_node = (is_bst_l and is_bst_r and
                       (max_l is None or self.key > max_l) and
                       (min_r is None or self.key < min_r))

        min_key = min(TreeNode.remove_none([min_l, self.key, min_r]))
        max_key = max(TreeNode.remove_none([max_l, self.key, max_r]))
        return is_bst_node, min_key, max_key

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

    @staticmethod
    def remove_none(nums):
        return [x for x in nums if x is not None]
