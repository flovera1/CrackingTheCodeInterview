'''
Transitive Closure
Given a directed graph, find out if a vertex v is reachable from another vertex u
for all pairs (u,v). Here reachable mean that there is a path from vertex u to v.
The reach-ability matrix is called transitive closure of a graph.


We will create a matrix that has the transitive closure of the graph. 
We need to call dfs for every node of graph to mark reachable vertices. 
The only way we dont call dfs is if we have it already in the transitive closure. 
'''
from collections import defaultdict

class Graph:
	def __init__(self, valNumVertices):
		self.vVertex = valNumVertices
		self.vGraph = defaultdict(list) # we store the graph as a default dictionary with list
										# of nodes for a node
		self.vTransitiveClosure = [[0 for j in range(self.vVertex)] for i in range(self.vVertex)]


	def addEdge(self, vU, vV):
		self.vGraph[vU].append(vV)

	def dfs(self, vSource, vDestiny):
		# mark reachability from source to destiny
		self.vTransitiveClosure[vSource][vDestiny] = 1
		for i in self.vGraph[vDestiny]:

			if self.vTransitiveClosure[vSource][vDestiny] == 0:
				self.dfs(vSource, i)

	# transitive closure:
	def transitiveClosure(self):
		for i in range(0, self.vVertex):
			self.dfs(i,i)

		print(self.vTransitiveClosure)

g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
g.transitiveClosure(); 

