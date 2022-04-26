class Graph:
    def __init__(self):
        self.graph = {}

    def addVertices(self,n):
        for i in range (0,n):
            self.graph[i] =[]
    
    def addEdges(self,u,v):

        if u in self.graph.keys() and v in self.graph.keys():
            self.graph[u].append(v)
            self.graph[v].append(u)
            return True
        return False

    
    def dfsHelper(self,s,visited):
        
        print(s ,end="")
        visited[s] = True
        for i in self.graph[s]:
            if visited[i] == False:
                self.dfsHelper(i,visited)

    def dfs(self,s=0):
        visited = [False] *(len(self.graph))
         #queue.append(s)
        for item in range(len(self.graph)):
            if visited[item] == False:
                self.dfsHelper(item,visited)





gr = Graph()
gr.addVertices(5)
gr.addEdges(0,2)
gr.addEdges(2,3)
gr.addEdges(1,3)
gr.addEdges(0,1)
gr.addEdges(4,1)
gr.addEdges(3,4)
print(gr.graph)
gr.dfs(0)
        