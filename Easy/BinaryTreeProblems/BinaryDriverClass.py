""""IMPORITING CLASSES WHICH HAS TO BE USED TO DRIVE THEM"""
from NodeStructure import Node
from BinaryTreeClass import  BinaryTree


#<-3->implementing the binary tree
#<-3.1-> connnecting links

#             4
#           /   \
#          2     6
#         / \   /  \
#        1   3  5   7

binaryTree = BinaryTree()
binaryTree.root = Node('4')
binaryTree.root.left = Node('2')
binaryTree.root.right = Node('6')
binaryTree.root.left.left = Node('1')
binaryTree.root.left.right = Node('3')
binaryTree.root.right.right = Node('7')
binaryTree.root.right.left = Node('5')

binaryTree1 = BinaryTree()
binaryTree1.root = Node('4')
binaryTree1.root.left = Node('2')
binaryTree1.root.left.left = Node('1')
binaryTree1.root.left.right = Node('3')
binaryTree1.root.right = Node('6')
binaryTree1.root.right.right = Node('7')
binaryTree1.root.right.left = Node('5')



""" assigning root value of tree in variable"""
a=binaryTree.root
#preorderTraversal of binary tree : root-left-right
print('\n')
print ("preorderList ->",binaryTree.preorderTraversal(a,binaryTree.preorderList))

#PostorderTraversal of binary tree : left-right-root
print('\n')
print ("PostorderTraversal ->",binaryTree.postorderTraversal(a,binaryTree.postorderList))

#InorderTraversal of binarey tree left:root:rigth
print('\n')
print ("InorderTraversal ->",binaryTree.InorderTraversal(a,binaryTree.inorderList))

#TotalnonLeafNode of binary tree
print('\n')
print("countOfNonLeafNode->",len(binaryTree.countOfNonLeafNode(a)))

#TotalLeafNode of binary tree
print('\n')
print("countOfLeafNode->",len(binaryTree.countOfLeafNode(a)))

#Total height  of binary tree
print('\n')
print("Height of Binary->",binaryTree.hightOfBinarytree(a))

#Check Strit binary trre exactly 0 or 2 children
print('\n')
print("Is it a StrictBinaryTree",binaryTree.checkStrictBinarytree(a))

#Diameter  of binary tree
print('\n')
print("Diameter of Binary 1->",binaryTree.diameterOfbinarytree(a))

#Total Diameter  of binary tree
print('\n')
print("Diameter of Binary 2->",binaryTree.optimizedDiameterOfBinaeryTree(a))

# level order Traversal of binary treee
print('\n')
print("levelorderTraversal ->",binaryTree.levelorderTraversal(a))

# all path root to leaf
print('\n')
b=binaryTree.path
c=BinaryTree.listOfPath
print("DetermindAllPathRootToLeaf ->",binaryTree.DetermindAllPathRootToLeaf(a,b))

# Find Mininum Node value in binary trree
print('\n')
print("findMinOnBT ->",binaryTree.findMinOnBT(a))

# Find Maximum Node value in binary trree
print('\n')
print("findMaxonBt ->",binaryTree.findMaxonBt(a))

# Find Least comman ancesstor
print('\n')
print("GetLCA ->",binaryTree.GetLCA(a,'1','7'))

#Check if it is valid binary tree or NodeStructure
print('\n')
Min=binaryTree.findMinOnBT(a)
Max= binaryTree.findMaxonBt(a)
print("IsValidBst ->",binaryTree.IsValidBst(a,Max,Min))

#Check if two binary tree isStructurallyIdentical or not
print('\n')
print("isStructurallyIdentical ->",binaryTree.isStructurallyIdentical(a,binaryTree1.root))

# for finding the deepest node of the binary tree.
print('\n')
print("deepest Node of Tree is ->",binaryTree.deepestNode(a))

# finding the number of leaves in the binary tree without using recursion.
print('\n')
print("numberOfLeaveslnBTusingLevelOrder->",binaryTree.numberOfLeaveslnBTusingLevelOrder(a))

# finding the number of (nodes with only with one child)
print('\n')
print("numberOfHalfNodeslnBTusingLevelOrder->",binaryTree.numberOfHalfNodeslnBTusingLevelOrder(a))
