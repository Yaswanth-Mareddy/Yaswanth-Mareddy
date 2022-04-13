import sys
from turtle import left

#lst_leaves=[]
class AVLTree:
    def __init__(self, root = None):
        self.root = root

    class AVLNode:
        def __init__(self, item, balance = 0, height=1,left = None, right = None):
            self.item = item
            self.left = left
            self.right = right
            self.balance = balance
            self.height=height
            
        def getHeight(node):
            if not node:
                return 0
            return node.height
        
        def getBalance(self):
            if not self:
                return 0
            return self.balance
        def setBalance(self,balance):
            self.balance = balance
        def __repr__(self):
            return f"AVLNode({repr(self.item)}, balance = {repr(self.balance)}, left = {repr(self.left)}, right = {repr(self.right)})"

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.item

            if self.right != None:
                for elem in self.right:
                    yield elem
        def get_leaves(self,node):
            # trivial case
            if node == None:
                return
            ### WRITE YOUR CODE HERE ###
            self.get_leaves(node.left)
            if(node.left==None and node.right==None):
                print(node.item, end = " ")
            self.get_leaves(node.right)
            
        def _getLeaves(self):
            # trivial case
            if self == None:
                return
            ### WRITE YOUR CODE HERE ###
            self.get_leaves(self)
        
    def insert(self, item):

        def rotateRight(pivot):
            # pivot becomes right child of bad child
            # bad child's right child becomes pivot's left child

            # get pivot's left child node (bad child)
            leftChild = pivot.left

            ### WRITE YOUR CODE HERE ###
            bad_child_right=leftChild.right
            leftChild.right=pivot
            pivot.left=bad_child_right
            #print(type(pivot.left))
            pivot.height=1+max(AVLTree.AVLNode.getHeight(pivot.left),AVLTree.AVLNode.getHeight(pivot.right))
            leftChild.height=1+max(AVLTree.AVLNode.getHeight(leftChild.left),AVLTree.AVLNode.getHeight(leftChild.right))
            # return bad child
            return leftChild
        
        def rotateLeft(pivot):
            # pivot becomes left child of bad child
            # bad child's left child becomes pivot's right child
            
            # get pivot's right child node (bad child)
            rightChild = pivot.right

            ### WRITE YOUR CODE HERE ###
            bad_child_left=rightChild.left
            rightChild.left=pivot
            pivot.right=bad_child_left
            pivot.height=1+max(AVLTree.AVLNode.getHeight(pivot.left),AVLTree.AVLNode.getHeight(pivot.right))
            rightChild.height=1+max(AVLTree.AVLNode.getHeight(rightChild.left),AVLTree.AVLNode.getHeight(rightChild.right))
            
            # return bad child
            return rightChild

        def __insert(root, item):
            # if empty tree, create a node with given item
            if root == None:
                return AVLTree.AVLNode(item)
            elif(item<root.item):
                root.left=__insert(root.left,item)
            else:
                root.right=__insert(root.right,item)
            root.height=1+max(AVLTree.AVLNode.getHeight(root.left),AVLTree.AVLNode.getHeight(root.right))
            balance_factor=AVLTree.AVLNode.getHeight(root.left)-AVLTree.AVLNode.getHeight(root.right)
            
            if(balance_factor>1 and item<root.left.item):
                return rotateRight(root)
            if(balance_factor<-1 and item>root.right.item):
                return rotateLeft(root)
            if(balance_factor>1 and item>root.left.item):
                root.left=rotateLeft(root.left)
                return rotateRight(root)
            if(balance_factor<-1 and item<root.right.item):
                root.right=rotateRight(root.right)
                return rotateLeft(root)
            # check if inserting duplicated value
            if(item==root.item):
                print(f"Insering duplicated value... {item}")
                raise Exception("Duplicate value")

            # once done __inserting return root
            return root
        
        # once done inserting update pivotFound value
        # and assign root with __insert return
        self.pivotFound = False
        self.root = __insert(self.root, item)

    # repr on tree calls repr on root node
    def __repr__(self):
        return f"AVLTree: {repr(self.root)}"

    # iter on tree calls iter on root node
    def __iter__(self):
        return iter(self.root)

    def __lookup(node, item):
        # returns True if value is in tree and False otherwise

        ### WRITE YOUR CODE HERE ###
        # returns True or False
        if(node==None):
            return False
        if(node.item==item):
            return True
        elif(item>node.item):
            return AVLTree.__lookup(node.right,item)
        else:
            return AVLTree.__lookup(node.left,item)

    def __contains__(self, item):
        # checks if item is in the tree
        # runs __lookup on the tree root
        return AVLTree.__lookup(self.root, item)

    def leaves(self):
        # finds tree leaves
        self.root._getLeaves()  

def main():
    tree = AVLTree()

    # get values from input file
    file = open(sys.argv[1], "r")
    for line in file:
        values = line.split()

    print(f"Values to be inserted: {values}")
    print()
    
    # insert values into the AVL tree
    for v in values:
        tree.insert(int(v))
        print(f"Value {v} is inserted.")
    print()

    # print out the tree
    print(repr(tree))
    print()
    
    # print out tree in-order traversal
    print("In-order traversal: ", end = "")
    for node in tree:
        print(node, end = " ")    
    print()

    # print out tree leaves
    print("\nLeaves: ", end = "")
    tree.leaves()
    print()
    
    # check if given values are in the tree
    print()
    for val in [10, 17, 35, 38, 40]:
        if (val in tree):
            print(f"Value {val} is in tree")
        else:
            print(f"Value {val} is not in tree")  

main()