class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []
            return True
        return False
    
    def add_edges(self,vert1,vert2):
        if vert1 in self.graph.keys() and vert2 in self.graph.keys():
            self.graph[vert1].append(vert2)
            self.graph[vert2].append(vert1)
            return True
        
        return False

    def remove_edges(self,vert1,vert2):
        if vert1 in self.graph.keys() and vert2 in self.graph.keys():
            self.graph[vert1].remove(vert2)
            self.graph[vert2].remove(vert1)
            return True
        
        return False

    def remove_vertex(self,vertex):

        if vertex in self.graph.keys():
            for vert in self.graph[vertex]:
                self.graph[vert].remove(vertex)
            del self.graph[vertex]
            return True
        return False
            
            

    
gr = Graph()

gr.add_vertex('A')
gr.add_vertex('B')
gr.add_vertex('C')
gr.add_vertex('D')

gr.add_edges('A','B')
gr.add_edges('B','C')
gr.add_edges('A','C')
gr.add_edges('A','D')
gr.add_edges('C','D')

gr.add_edges('E','A')

print(gr.graph)

gr.remove_edges('D','C')

print(gr.graph)

gr.remove_vertex('C')
print(gr.graph)