
class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.edges_graph = {}
        for start,end in self.edges:
            if start in self.edges_graph:
                self.edges_graph[start].append(end)
            else:
                self.edges_graph[start]=[end]
        print(self.edges_graph)

    def paths(self,start):
        if start in self.edges_graph:
            i=0
            self.destinations = []
            for destination in self.edges_graph[start]:
                self.destinations.append(destination)
                i+=1
            print(f'{i} flights from {start} to {self.destinations}')
        else:
            print(f'sorry there is no flight from {start}')



if __name__=='__main__':
    routes = [
        ('Mumbai','Paris'),
        ('Mumbai','Dubai'),
        ('Paris','Dubai'),
        ('Paris','Newyork'),
        ('Dubai','Newyork'),
        ('Newyork','Toronto')
    ]

    route_graph=Graph(routes)
    route_graph.paths('Mumbai')