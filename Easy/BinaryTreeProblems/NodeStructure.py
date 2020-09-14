#<-1-> defining binary tree
class Node:

    def __init__(self, data, left=None, right=None):

        self.left = None

        self.data = data

        self.right = None
        
    def __str__(self):
        return f"Node {self.data}"
    
    
    
