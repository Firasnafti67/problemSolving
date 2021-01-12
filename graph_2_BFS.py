#BFS -> QUEUE & ITERATIONS

from collections import deque,defaultdict



graph = defaultdict(list)
v,e = map(int, input().split())

def bfs(graph, start, visited, 	path):
	queue = deque()
	path.append(start)
	queue.append(start)
	visited[start] = True
	while len(queue) != 0:
		tmp_node = queue.popleft()
		for neigbor in graph[tmp_node]:
			if visited[neigbor] == False:
				path.append(neigbor)
				queue.append(neigbor)
				visited[neigbor] = True
	return path
				
for i in range(e):
	u,v = map(str, input().split())
	graph[u].append(v)
	graph[v].append(u)

start = 'A'
path = []
visited = defaultdict(bool)
traversedpath = bsf(graph,start,visited,path)
print(traversedpath)