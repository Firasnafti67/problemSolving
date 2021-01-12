#Undirected Graph
#We are using here DFS which uses in here Stack and recursion 
#BFS uses QUEUE AND ITERATION
from collections import defaultdict




def dfs(graph, start, visited, path):
	path.append(start)
	visited[start] = True
	for neighbor in graph[start]:
		if visited[neighbor] == False:
			dfs(graph, neighbor,visited, path)
	return path

			


graph = defaultdict(list)
v,e = map(int, input().split())
for i in range(e):
	u,v = map(str, input().split())
	graph[u].append(v)
	graph[v].append(u)
for v in graph:
	print(v, " ",graph[v])

path = []
start = "A"
visited = defaultdict(bool)
traversedpath = dfs(graph, start, visited, path)

print(traversedpath)