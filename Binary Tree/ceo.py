class TreeNode:
    def __init__(self,*data):
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

    def print_tree(self,info):

        if info=="name":
            space="|__" * self.get_level()
            print(space+self.data[0])
            for child in self.children:
                child.print_tree('name')

        elif info== "designation":
            space="|__" * self.get_level()
            print(space+self.data[1])
            for child in self.children:
                child.print_tree('designation')

        else:
            space="|__" * self.get_level()
            print(space+self.data[0] +" "+ "("+self.data[1]+")" )
            for child in self.children:
                child.print_tree('both')



def build_company_tree():

    root=TreeNode("Nilupul","CEO")

    Chinamay = TreeNode('Chinmay','CTO')
    
    Vishwa = TreeNode("Vishwa","Infrastructure Head")
    Vishwa.add_child(TreeNode("Dhaval","Cloud Manager"))
    Vishwa.add_child(TreeNode("Abijit","App Manager"))

    Aamir=TreeNode("Aamir","Application Head")

    Chinamay.add_child(Vishwa)
    Chinamay.add_child(Aamir)
    
    Gels=TreeNode("Gels","HR Head")
    Gels.add_child(TreeNode('Peter','Recuirment Manager'))
    Gels.add_child(TreeNode('Waqas','Policy Manager'))



    root.add_child(Chinamay)
    root.add_child(Gels)

    return root




if __name__ == '__main__':
    root_node = build_company_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy

        