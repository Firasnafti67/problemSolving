#Weighted DIRECTED GRAPH
import heapq
from collections import defaultdict




def shortestPath(graph, src, des):
	h = []

	heapq.heappush(h, (0, src))
	while len(h)!=0:
		currcost, currvtx = heapq.heappop(h)
		if currvtx == dest:
			print("Path from {} to {} with cost {}".format(src, dest, currcost))
			break
		for neig, neigborcost in graph[currvtx]:
			heapq.heappush(h,(currcost + neigborcost, neig))



graph = defaultdict(list)
v,e = map(int, input().split())
for i in range(e):
	u,v,w = map(str, input().split())
	graph[u].append((v,int(w)))

src, des = map(str, input().split())
shortestPath(graph, src, des)