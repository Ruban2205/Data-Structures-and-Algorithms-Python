# Implementation of Binary Search Tree 

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,node):
        if self.root is None:
            self.root = node
        else:
            temp = self.root
            prev = temp

            while temp:
                if node.data > temp.data:
                    prev = temp
                    temp = temp.right
                elif node.data < temp.data:
                    prev = temp
                    temp = temp.left

            if node.data < prev.data:
                prev.left = node
            elif node.data > prev.data:
                prev.right = node

    def inorder(self,temp):
        if temp.left is not None:
            self.inorder(temp.left)
        print(temp.data,end = ' ')
        if temp.right is not None:
            self.inorder(temp.right)

    def preorder(self,temp):
        print(temp.data,end = ' ')
        if temp.left is not None:
            self.preorder(temp.left)
        if temp.right is not None:
            self.preorder(temp.right)

    def postorder(self,temp):
        if temp.left is not None:
            self.postorder(temp.left)
        if temp.right is not None:
            self.postorder(temp.right)
        print(temp.data,end = ' ')

obj = BinarySearchTree()
print("BINARY SEARCH TREE\n")
while(True):
    print("\n1. INSERT DATA")
    print("2. INORDER DISPLAY")
    print("3. PREORDER DISPLAY")
    print("4. POSTORDER DISPLAY")
    print("5. EXIT\n")

    choice=int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter the data to be inserted:"))
        obj.insert(node(data))
        print(data, " Inserted Successfully!!")
  
    elif choice == 2:
        print("INORDER: ",end="")
        obj.inorder(obj.root)
        print()

    elif choice == 3:
        print("PREORDER: ",end="")
        obj.preorder(obj.root)
        print()

    elif choice == 4:
        print("POSTORDER: ",end="")
        obj.postorder(obj.root)
        print()

    elif choice == 5:
        break

    else:
        print("INVALID INPUT!!!")
        continue
