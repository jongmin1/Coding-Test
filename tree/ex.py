from node import Node

def preorder(tree):
    if tree:
        print(tree.key, end = ' ')
        preorder(tree.left)
        preorder(tree.right)
        
if __name__ == '__main__':
    root = Node('A')
    root.insertLeft('B')
    root.insertRight('C')
    root.left.insertLeft('D')
    root.left.insertRight('E')
    root.right.insertRight('G')
    root.left.left.insertLeft('H')
    preorder(root)