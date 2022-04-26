class Tree:
    def __init__(self,root):
        self.root = root
        self.left=None
        self.right = None
    
def maxDepth(node):
    if node is None:
        return -1 
 
    else :
 
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
 
 
# Driver program to test above function
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.left.right = Tree(6)
 
 
print ("Height of tree is %d" %(maxDepth(root)))

