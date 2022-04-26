class Graph:
    def __init__(self):
        self.gr={}
        

    def addVertices(self,v):
        self.size=v
        for i in range(v):
            self.gr[i+1]=[]
        return True
    
    def addEdges(self,u,v):
        if u in self.gr and v in self.gr:
            self.gr[u].append(v)
            self.gr[v].append(u)
            return True
        return False

    def dfsHelper(self, temp, item, visited):
        visited[item] = True
        temp.append(item)
        # print(temp)
        for i in self.gr[item]:
            # print(i)
            if visited[i] == False:
                temp = self.dfsHelper(temp, i, visited)
        
        return temp

    def connectedCheck(self):
        visited={i:False for i in self.gr.keys()}
        result=[]
        finalResult=[]
        max_size=0
        # print(visited)

        for item in range(1,self.size+1):
            if visited[item] == False:
                temp = []
                result.append(self.dfsHelper(temp, item, visited))
        
        finalResult.append(len(result))

        for item in result:
            if len(item) > max_size:
                max_size= len(item)
        
        finalResult.append(max_size)
        return finalResult

    def bfs(self):
        visited={i:False for i in self.gr.keys()}
        queue=[]
        result=[]
        finalResult=[]
        max_size=0
        
        for i in self.gr.keys():
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                temp=[]
                while queue:
                    itm=queue.pop(0)
                    temp.append(itm)
                    for i in self.gr[itm]:
                        if visited[i] == False:
                            queue.append(i)
                            visited[i]= True
                result.append(temp)
        
        finalResult.append(len(result))

        for item in result:
            if len(item) > max_size:
                max_size= len(item)
        
        finalResult.append(max_size)
        return finalResult


                

                


graph=Graph()
v,e= (input("").split())
# print(v," ",e)
graph.addVertices(int(v))
# print("Provide ",e," edges details:")
for i in range(int(e)):
    e1,e2 = (input("").split())
    graph.addEdges(int(e1),int(e2))
# print(" ")
# res =graph.connectedCheck()
# for itm in res:
#     print(itm)

res=graph.bfs()
for itm in res:
    print(itm)

