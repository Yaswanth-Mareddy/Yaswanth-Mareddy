from ast import get_source_segment
import sys

class Graph:

    def __init__(self):
        self.verList = {}
        self.numVertices = 0

    class __Vertex:
        def __init__(self, key):
            self.id = key       
            self.connectedTo = {} 

        def getId(self):
            return self.id

        def getConnections(self):
            return self.connectedTo.keys()

        def getWeight(self, nbr):
            return self.connectedTo[nbr] 

        def addNeighbor(self, nbr, weight = 0):
            self.connectedTo[nbr] = weight

        def __str__(self):
            return f"connected to: {str([x.id for x in self.connectedTo])}"   

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Graph.__Vertex(key)
        self.verList[key] = newVertex 
        return newVertex

    def getVertex(self, n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.verList

    def addEdge(self, source, destination, weight = 0):
        if source not in self.verList:
            newVertex = self.addVertex(source)
        if destination not in self.verList:
            newVertex = self.addVertex(destination)
        self.verList[source].addNeighbor(self.verList[destination], weight)
    
    def getVertices(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())

    def dfs(self, s, visited = None):
        if visited is None:
            visited = set()

        if s not in visited:
            print(s, end = " ")
            visited.add(s)
            for next_node in [x.id for x in self.verList[s].connectedTo]:
                self.dfs(next_node, visited)        

    def bfs(self, s, visited = None):
        if visited is None:
            visited = set()

        q = Queue()
        q.put(s)
        visited.add(s)

        while not q.empty():
            current_node = q.get()
            print(current_node, end = " ")

            for next_node in [x.id for x in self.verList[current_node].connectedTo]:
                if next_node not in visited:
                    q.put(next_node)
                    visited.add(next_node)

    def kruskals(self):
        vertices_sets = set()
        edges_dict = dict()
        MST = set()
        ### WRITE YOUR CODE HERE ###
        for vertex in self.getVertices():
            #print(iter(self.verList[vertex].getConnections()))
            source=self.getVertex(vertex)
            for k in self.verList[vertex].getConnections():
                #print(k)
                #print(vertex)
                
                edge=str(vertex)+","+str(k.getId())
                #print(edge)
                edges_dict[edge]=source.getWeight(k)
            source_set=frozenset({vertex})
            vertices_sets.add(source_set)
        print(vertices_sets)
        #print(edges_dict)
        edges_dict=sorted(edges_dict.items(), key=lambda x: x[1])
        print(edges_dict)
        for key,value in edges_dict:
            print("key ",key)
            print("value ",value)
            source=int(key.split(',')[0])
            destination=int(key.split(',')[1])
            source_set=self.get_set(source,vertices_sets)
            print("Source set",source_set)
            destination_set=self.get_set(destination,vertices_sets)
            print(destination_set)
            if(source_set!=destination_set):
                mst=("("+key+")",value)
                MST.add(mst)
                vertices_sets=self.merge_set(source_set,destination_set,vertices_sets)
                print(vertices_sets)
        return MST
    
    def merge_set(self,source_set,destination_set,vertices_sets):
        final_set=source_set.union(destination_set)
        vertices_sets.remove(source_set)
        vertices_sets.remove(destination_set)
        vertices_sets.add(final_set)
        return vertices_sets
    
    def get_set(self,vertex,vertices_sets):
        print("vertex",vertex)
        #print(vertices_sets)
        for vertex_set in vertices_sets:
            #print(vertex_set)
            if(vertex in vertex_set):
                return vertex_set

def printAdjMatrix(graph:Graph):
    vertices_lst=graph.getVertices()
    for vertex in vertices_lst:
        print(vertex,graph.getVertex(vertex))
        
    

def main():
    
    # create an empty graph
    graph = Graph()

    # get graph vertices & edges from input file and add them to the graph
    file = open(sys.argv[1], "r")
    for line in file:
        values = line.split()
        graph.addEdge(int(values[0]), int(values[1]), int(values[2]))
        graph.addEdge(int(values[1]), int(values[0]), int(values[2]))   

    # print adjacency list representation of the graph
    print()
    ### WRITE YOUR CODE HERE ###
    printAdjMatrix(graph)
    # create graph MST
    MST = graph.kruskals()
    # print graph MST
    print()    
    print("Graph MST:")
    print("Edge\t\tWeight")
    for edge in MST:
        print(f"{edge[0]}\t\t{edge[1]}")

main() 
    