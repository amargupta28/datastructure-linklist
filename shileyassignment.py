class Graph:
    def __init__(self):
        self.graph = {}

    def addVertices(self,n):
        for i in range (1,n+1):
            self.graph[i] =[]
    
    def addEdges(self,u,v):

        if u in self.graph.keys() and v in self.graph.keys():
            self.graph[u].append(v)
            self.graph[v].append(u)
            return True
        return False

    def noComp(self,s=1):
         visited = [False] *(len(self.graph))
         queue =[]
         visited[s-1] = True
         queue.append(s)
         print(visited)

         while queue:
             item=queue.pop(0)
             print(item, end=" ")

             for i in self.graph[item]:
                 if visited[i-1] == False:
                     visited[i-1] =True
                     queue.append(i)



gr = Graph()
gr.addVertices(4)
gr.addEdges(1,2)
gr.addEdges(2,3)
gr.addEdges(1,3)
print(gr.graph)
gr.noComp(3)
        