
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self):
        space="|__ __"* self.get_level()
        print(space+self.data)
        for child in self.children:
            child.print_tree()
            
            

def bulid_product_tree():

    root = TreeNode("Electronics")

    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("Mac book"))
    laptop.add_child(TreeNode("Microsoft"))
    laptop.add_child(TreeNode('Think pad'))


    cell_phone = TreeNode('cell_phone')
    cell_phone.add_child(TreeNode('iphone'))
    cell_phone.add_child(TreeNode('Google'))
    cell_phone.add_child(TreeNode('Vivo'))

    tv = TreeNode("TV")
    tv.add_child(TreeNode('Sumsung'))
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)
    root.add_child(cell_phone)
    root.add_child(tv)

    root.print_tree()


if __name__== "__main__" :
    bulid_product_tree()
    


