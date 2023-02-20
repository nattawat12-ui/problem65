class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data
    def insert(self,data):
        #compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left  is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
#Print the tree 
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
# serching
    def findval(self,lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+ " not found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data)+ ' is found')
# Inorder traversal 
#left --> Root --> Right 
    def inorderTraversal(self,root):
        res = []
        if root :
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res+ self.inorderTraversal(root.right)
        return res
     #Preorder \
    def PreorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res+ self.PreorderTraversal(root.left)
            res = res+self.PreorderTraversal(root.right)
        return res
    def PostorderTraversal(self,root):
        res= []
        if root :
             res  = self.PostorderTraversal(root.left)
             res = res + self.PostorderTraversal(root.right)
             res.append(root.data)    
        return res   
    def Deletenode(root, data):
        if root is None :
            return root
        if data < root.data:
            root.left = Deletenode(root.right, data)
        elif data > root.data:
            root 
        

root  = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)
root.PrintTree()
print(root.inorderTraversal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))
print(root.findval(7))
print(root.findval(35))

