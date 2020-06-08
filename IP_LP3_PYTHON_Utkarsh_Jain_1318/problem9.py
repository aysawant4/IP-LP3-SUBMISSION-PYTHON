class Node:  
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None
      
def isBST(root, prev): 
      
   
    if (root != None): 
        if (isBST(root.left, prev) == True): 
            return False
  
        if (prev != None and root.data <= prev.data): 
            return False
  
        prev = root 
        return isBST(root.right, prev) 
      
    return True
  
root = Node(3)  
root.left = Node(2)  
root.right = Node(5)  
root.right.left = Node(1)  
root.right.right = Node(4)  

if (isBST(root,None) == None): 
    print("true") 
else: 
    print("false") 
