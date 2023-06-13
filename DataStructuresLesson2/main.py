from User import User
from UserDatabase import UserDatabase
from TreeNode import TreeNode
from BSTNode import BSTNode
from TreeMap import TreeMap

database1 = UserDatabase()
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
atahan = User('atahan', 'Atahan Erdurak', 'atahanerdurak@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]
database1.insert(users)
# print(database1.list_all())


# tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
# tree2 = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth'), 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
# tree = TreeNode.parse_tuple(tree_tuple)
# print(tree)
# tree.display_keys()
# print(tree.tree_height_max())
# print(tree.tree_height_min())
# print(tree.tree_diameter())
# print(tree.preordertraversal())
# print(tree.postordertraversal())
# print(tree.inordertraversal())
# print(tree.tree_to_tuple())
# print(tree.is_bst())
# print(tree2.is_bst())

# bst_tree = BSTNode(jadhesh.username, jadhesh)
# bst_tree.insert(biraj.username, biraj)
# bst_tree.insert(sonaksh.username, sonaksh)
# bst_tree.insert(aakash.username, aakash)
# bst_tree.insert(hemanth.username, hemanth)
# bst_tree.insert(siddhant.username, siddhant)
# bst_tree.insert(vishal.username, siddhant)
# bst_tree.display_keys()
#
# node = bst_tree.find('hemanth')
# print(node.key, node.value)
#
# bst_tree.update('hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))
# node = bst_tree.find('hemanth')
# print(node.key, node.value)
# print(bst_tree.list_all())
# print(bst_tree.is_balanced())
#
# data = [(user.username, user) for user in users]
# print(data)
# tree = BSTNode.make_balanced_bst(data)
# tree.display_keys()


# bst_tree = BSTNode(users[0].username, users[0])
# for user in users:
#     bst_tree.insert(user.username, user)
# bst_tree.display_keys()
# bst_tree = bst_tree.balance_bst()
# bst_tree.display_keys()

treemap = TreeMap()
treemap.display()
for user in users:
    treemap[user.username] = user

treemap.display()
print(treemap['jadhesh'])
print(len(treemap))
for key, value in treemap:
    print(key, value)
print(list(treemap))

treemap['aakash'] = User(username='aakash', name='Aakash N S', email='aakashns@example.com')
print(treemap['aakash'])