class Graph:

    def __init__(self):
        self.graph={}
    
    def add_vertex(self,vertex):
        self.graph[vertex]=[]
        return True
    
    def add_edges(self,vert1,vert2,wt):
        if vert1 in self.graph.keys() and vert2 in self.graph.keys():
            self.graph[vert1].append([vert2,wt])
            self.graph[vert2].append([vert1,wt])
            return True
        return False
    
    def remove_edges(self,vert1,vert2):
        if vert1 in self.graph.keys() and vert2 in self.graph.keys():
            for i in self.graph[vert1]:
                if i[0] == vert2:
                    self.graph[vert1].remove(i)
                    break
            
            for i in self.graph[vert2]:
                if i[0] == vert1:
                    self.graph[vert2].remove(i)
                    break
            return True
        return False
    

gr =Graph()
gr.add_vertex('a')
gr.add_vertex('b')
gr.add_vertex('c')
gr.add_edges('a','b',2)
gr.add_edges('a','c',4)
gr.add_edges('b','c',1)

print(gr.graph)

gr.remove_edges('c','a')
print(gr.graph)



    
        

    

