class BinarySearchTree:
    def __init__(self,data) :
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if self.data==data:
            return # node already exist
        
        elif data<self.data:
            ##left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left= BinarySearchTree(data)

        else:
            ##right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right= BinarySearchTree(data)

    def in_order_transversal(self):
        elements=[]

        # visit left subtree
        if self.left:
            elements += self.left.in_order_transversal()

        elements.append(self.data)
        
        # visit right subtree
        if self.right:
            elements += self.right.in_order_transversal()

        return elements
            

    def search(self,val):
        if self.data==val:
            return True
        
        elif val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False


        



def build_tree(elements):
    print("Print tree with",elements)
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root




if __name__=='__main__':
    numbers= [ 87,45,67,24,56,78,89,90,2,1,4,5,6,7,8,90,67,5,4,56,7,87,89 ]
    root=build_tree(numbers)
    print("in order trasversal",root.in_order_transversal())
    print(root.search(0))
    pass
