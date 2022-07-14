

class BinarySearchTree:
    def __init__(self,data) :
        self.data=data
        self.left=None
        self.right=None



    def add_child(self,child):
        if self.data==child:
            return # node already exist
        
        elif child<self.data:
            ##left subtree
            if self.left:
                self.left.add_child(child)
            else:
                self.left= BinarySearchTree(child)

        else:
            ##right subtree
            if self.right:
                self.right.add_child(child)
            else:
                self.right= BinarySearchTree(child)



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

    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        #visit left subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        #visit right subtree
        if self.right:
            elements += self.right.pre_order_traversal()
        
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
        

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        elements = self.in_order_transversal()
        element = 0
        for i in range(0,len(elements)):
            element+=elements[i]
        return element
    
    def delete(self,number):
        if number<self.data:
            if self.left:
                self.left=self.left.delete(number)
        elif number>self.data:
            if self.right:
                self.right=self.right.delete(number)
        else:
            if self.left is None and self.right is None :
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            
            # Find minimum from left subtree and paste in place of node
            #min_val=self.right.find_min()
            #self.data=min_val
            #self.right=self.right.delete(min_val)

            max_val=self.left.find_max()
            self.data=max_val
            self.left=self.left.delete(max_val)
        return self   


def build_tree(elements):
    print("Print tree with",elements)
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root




if __name__=='__main__':
    #numbers= [ 87,45,67,24,56,78,89,90,876,-123,2,1,8,90,67,56,87,89,2 ]
    numbers=["Ajay","vijay",'abhishek','chintu','neetu','manish','mom','dad']
    root=build_tree(numbers)
    print("in order trasversal",root.in_order_transversal())
    #print(root.search(0))
    print('min:',root.find_min())
    #print("max:",root.find_max())
    #print(root.calculate_sum())
    print("pre order transversal",root.pre_order_traversal())
    print(root.delete('Ajay'))
    print("in after delete",root.in_order_transversal())
    pass
