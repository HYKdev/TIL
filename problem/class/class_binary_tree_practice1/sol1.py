import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def preorder(self, n):
        if n!= None:
            print(n.item, '', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def levelorder(self, n):
        q = []
        q.append(n)
        while q:
            t = q.pop(0)
            print(t.item, '', end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

T = int(input())
for tc in range(1, T + 1):
    number = int(input())
    tree = BinaryTree()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n11 = Node(11)
    n12 = Node(12)
    n13 = Node(13)

    tree.root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.left = n5
    n3.right = n6
    n4.left = n7
    n5.left = n8
    n5.right = n9
    n6.left = n10
    n6.right = n11
    n7.left = n12
    n11.right = n13

    tree.preorder(tree.root)
    print()
    tree.levelorder(tree.root)


import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    
    print(f'#{tc} ')

